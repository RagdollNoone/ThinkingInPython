from django import forms
from Django.meet.base_model.models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
