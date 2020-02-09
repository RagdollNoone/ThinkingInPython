from base_model.models import User, Sign, Meet, Room, Group
import copy


# TODO: 处理record为空的情况


class Result:
    __ret = {}
    __result = None

    def __init__(self):
        return

    def get_ret(self):
        return self.__ret


class SignResult(Result):
    __sign_record = None

    def __init__(self, result, sign_record):
        is_result = isinstance(result, Result)
        is_sign_record = isinstance(sign_record, Sign)
        if is_result and is_sign_record:
            self.__result = result
            self.__sign_record = sign_record
        else:
            print("Class SignResult, Function __init__,"
                  " CORRECT RESULT: " + is_result +
                  " CORRECT SIGN RECORD: " + is_sign_record)

    def get_ret(self):
        ret = copy.copy(self.__result.get_ret())

        ret['meet'] = self.__sign_record.meet.to_json()
        ret['user'] = self.__sign_record.user.to_json()
        ret['sign_state'] = self.__sign_record.sign_state
        ret['sign_time'] = str(self.__sign_record.sign_time.strftime("%H:%M:%S"))

        return ret


class MeetResult(Result):
    __meet_record = None

    def __init__(self, result, meet_record):
        is_result = isinstance(result, Result)
        is_meet_record = isinstance(meet_record, Meet)
        if is_result and is_meet_record:
            self.__result = result
            self.__meeting_record = meet_record
        else:
            print("Class MeetingResult, Function __init__,"
                  " CORRECT RESULT: " + is_result +
                  " CORRECT MEETING RECORD: " + is_meet_record)

    def get_ret(self):
        ret = copy.copy(self.__result.get_ret())

        ret['subject'] = self.__meeting_record.subject
        ret['start'] = str(self.__meeting_record.start.strftime("%H:%M:%S"))
        ret['end'] = str(self.__meeting_record.end.strftime("%H:%M:%S"))
        ret['room'] = self.__meeting_record.room.to_json()
        ret['organizer'] = self.__meeting_record.organizer.to_json()
        participant_list = self.__meeting_record.participant.all()
        participant_ret = []
        for participant in participant_list:
            participant_ret.append(participant.to_json())
        ret['participant'] = participant_ret

        return ret


class UserResult(Result):
    __user_record = None

    def __init__(self, result, user_record):
        is_result = isinstance(result, Result)
        is_user_record = isinstance(user_record, User)
        if is_result and is_user_record:
            self.__result = result
            self.__user_record = user_record
        else:
            print("Class UserResult, Function __init__,"
                  " CORRECT RESULT: " + is_result +
                  " CORRECT USER RECORD: " + is_user_record)

    def get_ret(self):
        ret = copy.copy(self.__result.get_ret())

        ret['wechat_id'] = self.__user_record.wechat_id
        ret['name'] = self.__user_record.name
        ret['email'] = self.__user_record.email
        ret['group'] = self.__user_record.group.to_json()

        return ret


class GroupResult(Result):
    __group_record = None

    def __init__(self, result, group_record):
        is_result = isinstance(result, Result)
        is_group_record = isinstance(group_record, Group)
        if is_result and is_group_record:
            self.__result = result
            self.__group_record = group_record
        else:
            print("Class UserResult, Function __init__,"
                  " CORRECT RESULT: " + is_result +
                  " CORRECT GROUP RECORD: " + is_group_record)

    # def __get_group_user_statistics__(self):
    #     ret = []
    #     user_list = User.Objects.filter(group__name=self.__group_record.name).all()
    #
    #     for user in user_list:
    #         result = Result()
    #         result = UserResult(result, user)
    #         ret.append(copy.copy(result.get_ret()))
    #
    #     return ret

    def get_ret(self):
        ret = copy.copy(self.__result.get_ret())

        ret['name'] = self.__group_record.name
        # ret['user_list'] = self.__get_group_user_statistics__()

        return ret


class RoomResult(Result):
    __room_record = None

    def __init__(self, result, room_record):
        is_result = isinstance(result, Result)
        is_room_record = isinstance(room_record, Room)
        if is_result and is_room_record:
            self.__result = result
            self.__room_record = room_record
        else:
            print("Class UserResult, Function __init__,"
                  " CORRECT RESULT: " + is_result +
                  " CORRECT ROOM RECORD: " + is_room_record)

    def get_ret(self):
        ret = copy.copy(self.__result.get_ret())

        ret['name'] = self.__room_record.name

        return ret
