from enum import Enum, unique


@unique
class SignState(Enum):
    UN_SIGN = 0,  # 会议尚未开始 且未签到
    SIGNED = 1,  # 正常签到成功
    LATE = 2,  # 迟到
    MISS = 3,  # 会议结束且未签到
    REFUSE = 4,  # 拒绝会议
    pass
