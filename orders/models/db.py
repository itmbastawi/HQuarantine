from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.


class item_type(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):

        return self.name


class service_table(models.Model):
    type_id = models.ForeignKey(item_type,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    quantity= models.IntegerField()
    notes = models.TextField()
    stop = models.BooleanField(default=False)
    created_user = models.ForeignKey(User,on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return self.name


class action_list(models.Model):
    name=models.CharField(max_length=25)
    def __str__(self):

        return self.name

        
time_list =[
    (10,'10 دقايق'),
    (15, '15 دقيقة'),
    (30 , 'نصف ساعة'),
    (60 , 'ساعة'),
    (120 ,'ساعتين')
]

class item_action(models.Model):
    action_id = models.ForeignKey(action_list,on_delete=models.CASCADE)
    service_id = models.ForeignKey(service_table,on_delete=models.CASCADE)
    delivery_time  = models.CharField(max_length=5,choices=time_list)
    created_user = models.ForeignKey(User,on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)


class user_profile(models.Model):
    user_id = models.OneToOneField(User,on_delete=models.CASCADE)
    mobile = models.CharField(max_length=15)
    address = models.TextField()
    photo =  models.ImageField(default='avatar.jpg',upload_to='profile')
    created_on = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
            super().save(*args, **kwargs)
            img = Image.open(self.photo.path)
            output_size = (300, 350)
            img.thumbnail(output_size)
            img.save(self.photo.path)