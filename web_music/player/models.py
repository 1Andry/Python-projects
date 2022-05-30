from django.db import models
from django.contrib.auth.models import User


class AddSong(models.Model):
    song = models.FileField(upload_to='uploads/songs')

    class Meta:
        verbose_name = 'Песни'
        verbose_name_plural = 'Песни'
# class Profile(models.Model):
#     # user = models.CharField(max_length=255)
#     email = models.EmailField(max_length=255)
#     password1 = models.CharField(max_length=50)
#     password2 = models.CharField(max_length=50)
#     time_created = models.DateTimeField(auto_now=True)
#     song = models.FileField(upload_to='uploads/songs', blank=True)
#     photo = models.ImageField(null=True, blank=True, upload_to="images/")
#
#     def __str__(self):
#         return self.email
#
#     class Meta:
#         verbose_name = 'Профиль'
#         verbose_name_plural = 'Профиль'


# class Test(models.Model):
#     password1 = models.CharField(max_length=50)
#     password2 = models.CharField(max_length=50)
