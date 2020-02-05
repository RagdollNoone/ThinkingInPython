from django.db import models


# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    pass


class Group(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    pass


class User(models.Model):
    wechat_id = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    # password = models.CharField(max_length=255)
    group = models.OneToOneField(Group, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    @staticmethod
    def is_new_user(wechat_id):
        try:
            selected_user = User.Objects.get(pk=wechat_id)
        except (KeyError, User.DoesNotExist):
            return True
        else:
            return False  # 返回当前选中的人
    pass


class SuperUser(User):
    pass


class Meet(models.Model):
    organizer = models.OneToOneField(SuperUser, on_delete=models.CASCADE)
    room = models.OneToOneField(Room, on_delete=models.CASCADE)
    subject = models.CharField(max_length=255)
    start = models.DateTimeField('meet start time')
    end = models.DateTimeField('meet end time')

    def __str__(self):
        return self.subject

    pass


class Sign(models.Model):
    meet = models.OneToOneField(Meet, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    sign_state = models.IntegerField(default=0)
    sign_time = models.DateTimeField('sign time')

    pass




