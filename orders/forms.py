from django.forms import ModelForm
from .models import user_profile,service_table

class profile_form(ModelForm):
    class Meta:
        model= user_profile
        fields = ['mobile','address','photo']


class item_form(ModelForm):
    class Meta:
        model = service_table
        fields = ['type_id','name','quantity','notes']

