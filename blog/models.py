from django.db import models

# Create your models here.

class Contactus(models.Model):
    csno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    msg = models.TextField()

    def __str__(self):
        return self.email

class Post(models.Model):
    psno = models.AutoField(primary_key=True)
    category = models.CharField(max_length=225)
    title = models.CharField(max_length=255)
    imgurl = models.TextField()
    content = models.TextField()
    auther = models.CharField(max_length=13)
    slug = models.CharField(max_length=130)
    views = models.IntegerField(default=0)
    timestamp = models.DateTimeField(blank=True)

    def __str__(self):
        return self.title + ' by ' + self.auther

class Emails(models.Model):
    esno = models.AutoField(primary_key=True)
    email = models.EmailField()

    def __str__(self):
        return self.email
