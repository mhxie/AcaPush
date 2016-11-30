from django.db import models

# Create your models here.

class Academy(models.Model):
    name = models.CharField(max_length=255, default="SCU")
    address = models.CharField(max_length=255, default="www.scu.edu.cn")

    def __str__(self):
        return self.name

class News(models.Model):
    academy = models.ForeignKey(Academy, default=None)
    # academy = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    time = models.DateTimeField(null=True)
    # time = models.CharField(max_length=255)
    sourceURL = models.CharField(max_length=255)
    picURL_Path = models.CharField(max_length=255)
    originURL = models.CharField(max_length=255)
    accessNum = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class Notice(models.Model):
    academy = models.ForeignKey(Academy, default=None)
    #academy = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    time = models.DateTimeField(null=True)
    # time = models.CharField(max_length=255)
    sourceURL = models.CharField(max_length=255)
    originURL = models.CharField(max_length=255)
    accessNum = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class StudentInfo(models.Model):
    studentID = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(max_length=255)
    nickname = models.CharField(max_length=255, default='')
    lastModified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.studentID


class NewsComment(models.Model):
    news = models.ForeignKey(News, default=None)
    # academy = models.ForeignKey(Academy)
    studentInfo = models.ForeignKey(StudentInfo, default=None)
    content = models.CharField(max_length=255)
    time = models.DateTimeField(auto_now=True)
    ip = models.CharField(max_length=255)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)

    def __str__(self):
        return self.content
