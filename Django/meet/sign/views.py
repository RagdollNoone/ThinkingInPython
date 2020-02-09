import os
import sys

from base_model.models import User, Group, Room, Meet, Sign
from common.response import Response
from common.signstate import SignState
from common import utility
from django.utils import timezone


# Create your views here.
def test_response(request):
    response = Response()
    head = response.get_header()
    body = response.get_body()
    head['status'] = 'Process successfully'
    head['error_code'] = 0
    body['id'] = 1
    body['name'] = 'dendy'
    body['user'] = User.objects.get(name='n1').to_json()
    body['group'] = Group.objects.get(name='Engineering').to_json()
    body['room'] = Room.objects.get(name='xian').to_json()
    selected_meet = Meet.objects.get(subject='subject1')
    body['meet'] = selected_meet.to_json()
    body['sign'] = Sign.objects.get(meet=selected_meet, user__name='n1').to_json()
    result = response.construct_json_response()
    print(' File: ' + os.path.basename(__file__) +
          ' Func: ' + sys._getframe().f_code.co_name)


def is_new_user(request):
    if request.method == 'GET':
        wechat_id = request.GET['wechat_id']

        print('wechat_id: ' + wechat_id +
              ' File: ' + os.path.basename(__file__) +
              ' Func: ' + sys._getframe().f_code.co_name)

        result = Response()
        header = result.get_header()
        header['error_code'] = 0

        body = result.get_body()
    try:
        selected_user = User.objects.get(wechat_id=wechat_id)
    except (KeyError, User.DoesNotExist):
        header['status'] = 'NotExist'
        return result.construct_json_response()

    header['status'] = 'Exist'
    body['user'] = selected_user.to_json()

    return result.construct_json_response()


def add_user(request):
    if request.method == 'POST':
        result = Response()
        header = result.get_header()
        body = result.get_body()

        try:
            selected_group = Group.objects.get(name=request.POST['group'])
        except (KeyError, Group.DoesNotExist):
            header['error_code'] = -1
            header['status'] = 'Add user fail, please post a correct group name'
            return result.construct_json_response()

        new_user = User()
        new_user.wechat_id = request.POST['wechat_id']
        new_user.email = request.POST['email']
        new_user.group = selected_group
        new_user.save()

        header['error_code'] = 0
        header['status'] = 'Add user success'
        body['user'] = new_user.to_json()

        return result.construct_json_response()


def sign(request):
    if request.method == 'POST':
        result = Response()
        header = result.get_header()
        body = result.get_body()

        selected_user = User.objects.get(wechat_id=request.POST['wechat_id'])
        selected_meet = utility.find_meet_by_room(request.POST['room'])

        if selected_meet is None:
            header['error_code'] = -1
            header['status'] = 'Find meet by room fail'
            return result.construct_json_response()
        else:
            try:
                selected_sign = Sign.objects.get(meet=selected_meet, user=selected_user)
            except (KeyError, Sign.DoesNotExist):
                new_sign = Sign()
                new_sign.user = selected_user
                new_sign.meet = selected_meet
                if selected_meet.start < timezone.now():
                    new_sign.sign_state = SignState.LATE
                else:
                    new_sign.sign_state = SignState.SIGNED
                new_sign.sign_time = timezone.now()
                new_sign.save()

                header['error_code'] = 0
                header['status'] = 'Set SignState.SIGNED success'
                body['sign'] = new_sign.to_json()
                return result.construct_json_response()

            header['error_code'] = -1
            header['status'] = 'Sign fail, sign record has existed'
            return result.construct_json_response()


def get_user_today_meets(request):
    if request.method == 'GET':
        result = Response()
        header = result.get_header()
        body = result.get_body()

        date = timezone.now().date()
        selected_user = User.objects.get(email=request.GET['email'])
        selected_meet_list = selected_user.meet_set.all()
        selected_meet_ret = []
        for selected_meet in selected_meet_list:
            if selected_meet.start.strftime("%Y-%m-%d") == date:
                selected_meet_ret.append(selected_meet.to_json())

        header['error_code'] = 0
        header['status'] = 'Get user today meets success'
        body['meet'] = selected_meet_ret

        return result.construct_json_response()


def get_sign_statistics(request):
    if request.method == 'GET':
        result = Response()
        header = result.get_header()
        body = result.get_body()

        room_name = request.GET['room_name']
        start_time = request.GET['start_time']
        statistics_ret = utility.get_sign_statistics(room_name, start_time)

        header['error_code'] = 0
        header['status'] = 'Get sign statistics success'
        body['sign_statistics'] = statistics_ret

        return result.construct_json_response()


def refuse_attend(request):
    if request.method == 'POST':
        result = Response()
        header = result.get_header()
        body = result.get_body()

        room_name = request.GET['room_name']
        start_time = request.GET['start_time']
        selected_meet = utility.get_meet_by_room_and_start(room_name, start_time)

        selected_user = User.objects.get(email=request.GET['email'])

        selected_sign = Sign.objects.get(user=selected_user, meet=selected_meet)
        selected_sign.sign_state = SignState.REFUSE
        selected_sign.save()

        header['error_code'] = 0
        header['status'] = 'Refuse attend success'
        body['sign'] = selected_sign.to_json()

        return result.construct_json_response()


def add_new_user_attend(request):
    if request.method == 'POST':
        room_name = request.GET['room_name']
        start_time = request.GET['start_time']
        selected_meet = utility.get_meet_by_room_and_start(room_name, start_time)

        selected_user = User.objects.get(email=request.GET['email'])

        result = Response()
        header = result.get_header()
        body = result.get_body()

        try:
            selected_meet.organizer.all().get(wechat_id=selected_user.wechat_id)
        except (KeyError, User.DoesNotExist):
            selected_meet.organizer.add(selected_user)
            selected_meet.save()

            new_sign = Sign()
            new_sign.save(commit=False)
            new_sign.meet = selected_meet
            new_sign.user = selected_user
            new_sign.sign_state = SignState.SIGNED
            new_sign.sign_time = selected_meet.start
            new_sign.save()

            header['error_code'] = 0
            header['status'] = 'Add new user success for non-existent user'
            body['meet'] = selected_meet.to_json()
            body['sign'] = new_sign.to_json()
            return result.construct_json_response()
        else:
            try:
                selected_sign = Sign.objects.get(user=selected_user, meet=selected_meet)
            except (KeyError, Sign.DoesNotExist):
                header['error_code'] = -1
                header['status'] = 'Add new user can not add sign record for exist user'
                return result.construct_json_response()
            else:
                if selected_sign.sign_state == SignState.REFUSE:
                    selected_sign.sign_state = SignState.SIGNED

                    header['error_code'] = 0
                    header['status'] = 'Add new user success for existent user'
                    body['sign'] = selected_sign.to_json()
                    return result.construct_json_response()

                header['error_code'] = -1
                header['status'] = 'Add new user can not modify sign record for exist user'
                return result.construct_json_response()


def get_detail_groups(request):
    if request.method == "GET":
        result = Response()
        header = result.get_header()
        body = result.get_body()
        body['group'] = []

        for selected_group in Group.objects.all():
            temp_ret = selected_group.to_json()
            temp_ret['user'] = []
            for selected_user in User.objects.filter(group__name=selected_group.name):
                temp_ret['user'].append(selected_user.to_json())
            body['group'].append(temp_ret)

        header['error_code'] = 0
        header['status'] = 'Get detail groups success'
        return result.construct_json_response()




