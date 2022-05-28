from django.db import models


class Skill(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='skill/images/')
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title


class Test(models.Model):
    ti1 = models.CharField(max_length=200)
    ti2 = models.CharField(max_length=200)
