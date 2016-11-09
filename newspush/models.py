from django.db import models

# Create your models here.

class Academy(models.Model):
    # code = models.CharField(max_length=255)
    name = models.CharField(max_length=255, default="SCU")
    address = models.CharField(max_length=255, default="www.scu.edu.cn")

class News(models.Model):
    academy = models.ForeignKey(Academy, default=None)
    title = models.CharField(max_length=255)
    time = models.DateTimeField(null=True)
    sourceURL = models.CharField(max_length=255)
    picURL_Path = models.CharField(max_length=255)
    originURL = models.CharField(max_length=255)
    accessNum = models.IntegerField(default=0)

class Notice(models.Model):
    academy = models.ForeignKey(Academy, default=None)
    title = models.CharField(max_length=255)
    time = models.DateTimeField(null=True)
    sourceURL = models.CharField(max_length=255)
    originURL = models.CharField(max_length=255)
    accessNum = models.IntegerField(default=0)

class StudentInfo(models.Model):
    studentID = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(max_length=255)
    nickname = models.CharField(max_length=255, default='')
    lastModified = models.DateTimeField(auto_now=True)

class NewsComment(models.Model):
    news = models.ForeignKey(News, default=None)
    # academy = models.ForeignKey(Academy)
    studentInfo = models.ForeignKey(StudentInfo, default=None)
    content = models.CharField(max_length=255)
    time = models.DateTimeField(auto_now=True)
    ip = models.CharField(max_length=255)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
