from django.db import models


# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def to_json(self):
        from common.result import Result, RoomResult
        ret = Result()
        ret = RoomResult(ret, self)
        return ret.get_ret()


class Group(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def to_json(self):
        from common.result import Result, GroupResult
        ret = Result()
        ret = GroupResult(ret, self)
        return ret.get_ret()


class User(models.Model):
    wechat_id = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    # password = models.CharField(max_length=255)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def to_json(self):
        from common.result import Result, UserResult
        ret = Result()
        ret = UserResult(ret, self)
        return ret.get_ret()


class Meet(models.Model):
    organizer = models.ForeignKey(User, on_delete=models.CASCADE)
    participant = models.ManyToManyField(User)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    subject = models.CharField(max_length=255)
    start = models.DateTimeField('meet start time')
    end = models.DateTimeField('meet end time')

    def __str__(self):
        return self.subject

    def to_json(self):
        from common.result import Result, MeetResult
        ret = Result()
        ret = MeetResult(ret, self)
        return ret.get_ret()


class Sign(models.Model):
    meet = models.ForeignKey(Meet, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sign_state = models.IntegerField(default=0)
    sign_time = models.DateTimeField('sign time')

    def __str__(self):
        return "Subject: %s, User: %s, SignState: %d, SignTime: %s" % (self.meet.subject, self.user.name, self.sign_state, self.sign_time)

    def to_json(self):
        from common.result import Result, SignResult
        ret = Result()
        ret = SignResult(ret, self)
        return ret.get_ret()
