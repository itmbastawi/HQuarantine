from django.forms import ModelForm
from .models import user_profile

class profile_form(ModelForm):
    class Meta:
        model= user_profile
        fields = ['mobile','address','photo']