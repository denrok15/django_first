from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from users.models import Contr

User = get_user_model()

class UserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model= User


class ContrForm(ModelForm):
    class Meta:
        model = Contr
        fields = ["name"]
