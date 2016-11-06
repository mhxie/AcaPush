from django.db import models

# Create your models here.

class college(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    code = models.CharField(max_length=255)

class news(models.Model):
    collegeId = models.ForeignKey(college)
    title = models.CharField(max_length=255)
    time = models.DateField()
    sourceURL = models.CharField(max_length=255)
    picURL = models.CharField(max_length=255)
    originURL = models.CharField(max_length=255)
    accessNum = models.IntegerField()

class notice(models.Model):
    collegeId = models.ForeignKey(college)
    title = models.CharField(max_length=255)
    time = models.DateField()
    sourceURL = models.CharField(max_length=255)
    originURL = models.CharField(max_length=255)
    accessNum = models.IntegerField()

class studentInfo(models.Model):
    studentId = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    secondName = models.CharField(max_length=255)
    lastModified = models.DateField()

class newsComment(models.Model):
    newsId = models.ForeignKey(news)
    collegeId = models.ForeignKey(college)
    studentId = models.ForeignKey(studentInfo)
    sourceURL = models.CharField(max_length=255)
    time = models.DateField()
    ip = models.CharField(max_length=255)
    enjoy = models.IntegerField()
    dislike = models.IntegerField()


