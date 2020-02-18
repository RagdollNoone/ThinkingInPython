import datetime
import time

from base_model.models import User, Group, Room, Meet, Sign
from common.signstate import SignState


# 当前房间连着两场会议
# 且第一场会议只有半小时该怎么办
def find_meet_by_room(room_name):
    try:
        selected_room = Room.objects.get(name=room_name)
    except (KeyError, Room.DoesNotExist):
        return None

    selected_meet_list = Meet.objects.filter(room=selected_room)
    if len(selected_meet_list) == 0:
        return None
    else:
        now = datetime.datetime.now()
        start = (now - datetime.timedelta(minutes=30)).strftime("%Y-%m-%d %H:%M:%S")
        end = (now + datetime.timedelta(minutes=10)).strftime("%Y-%m-%d %H:%M:%S")

        for selected_meet in selected_meet_list:
            meet_start_time = selected_meet.start.strftime("%Y-%m-%d %H:%M:%S")
            if start <= meet_start_time <= end:
                return selected_meet

        return None


def get_meet_by_room_and_start(room_name, start_time):
    selected_meet_list = Meet.objects.filter(room__name=room_name)

    for selected_meet in selected_meet_list:
        if selected_meet.start.strftime("%H:%M:%S") == start_time:
            return selected_meet

    return None


def get_sign_statistics(room_name, start_time):
    selected_meet = get_meet_by_room_and_start(room_name, start_time)

    late_sign_number = 0
    sign_number = 0
    miss_sign_number = 0
    total_sign_number = 0
    selected_sign_ret = []
    statistics_ret = {}

    if selected_meet is not None:
        statistics_ret['meet'] = selected_meet.to_json()
        selected_sign_list = Sign.objects.filter(meet=selected_meet)

        for selected_sign in selected_sign_list:
            selected_sign_ret.append(selected_sign.to_json())
            sign_state = selected_sign.sign_state

            if sign_state == SignState.MISS.value[0]:
                miss_sign_number += 1
            elif sign_state == SignState.SIGNED.value[0]:
                sign_number += 1
            elif sign_state == SignState.LATE.value[0]:
                late_sign_number += 1

        total_sign_number = sign_number + miss_sign_number + late_sign_number
        statistics_ret['sign'] = selected_sign_ret
        statistics_ret['sign_num'] = sign_number
        statistics_ret['miss_num'] = miss_sign_number
        statistics_ret['late_num'] = late_sign_number
        statistics_ret['total'] = total_sign_number
        statistics_ret['proportion'] = round(((sign_number * 100 + late_sign_number * 100) / total_sign_number), 1)

    return statistics_ret
