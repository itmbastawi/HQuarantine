from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class item_type(models.Model):
    name = models.CharField(max_length=30)

class service_table(models.Model):
    type_id = models.ForeignKey(item_type,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    quantity= models.IntegerField()
    notes = models.TextField()
    stop = models.BooleanField()
    created_user = models.ForeignKey(User,on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)

action_list=(
            ('A','Accepted'),
            ('b','buy'),
            ('d','delivered')
            )

class item_action(models.Model):
    name = models.CharField(max_length=5,choices=action_list)
    service_id = models.ForeignKey(service_table,on_delete=models.CASCADE)
    delivery_time = models.DateTimeField()
    created_user = models.ForeignKey(User,on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)


class user_profile(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    mobile = models.CharField(max_length=15)
    address = models.TextField()
    photo =  models.FileField(upload_to='uploads/')
    created_on = models.DateTimeField(auto_now_add=True)
