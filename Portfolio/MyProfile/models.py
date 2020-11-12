from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Language(models.Model):
    language = models.CharField(max_length=20)

    def __str__(self):
        return self.language


class Basic_Information(models.Model):
    Gender = (
                 ('Male',"Male"),
                 ('Female',"Female"),
                 ('Others',"Others"),)
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_pics = models.ImageField(null=True, blank=True)
    Name = models.CharField(max_length=30,null=True)
    Phone = models.CharField(max_length=30,null=True)
    Location = models.CharField(max_length=40,null=True)
    Gender = models.CharField(max_length=30,choices=Gender)
    age = models.IntegerField(null=True, default=0)
    about = models.TextField(null=True,blank=True)
    Language = models.ManyToManyField(Language)

    def __str__(self):
        return '{0}'.format(self.username)


class Education(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    institution_name = models.CharField(max_length=200, null=True)
    Degree = models.CharField(max_length=200, null=True)
    Major = models.CharField(max_length=200, null=True)
    description = models.TextField(null=True)
    yearDuration = models.CharField(max_length=100, null=True, blank=True)
    result = models.FloatField(null=True)
    StartDate = models.DateField(null=True, blank=True)
    EndDate = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.institution_name

    def full_subject(self):
        return '{0} - {1}'.format(self.Degree,self.Major)

    def full_education_date(self):
        return '{0} - {1}'.format(self.StartDate,self.EndDate)


class Project(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    projectName = models.CharField(max_length=200, null=True)
    projectTools = models.CharField(max_length=200, null=True)
    projectDescription = models.TextField(null=True)
    projectGithub = models.URLField(null=True,blank=True)
    projectDemo = models.URLField(null=True,blank=True)
    projectImage = models.ImageField(upload_to='Project Image',null=True, blank=True)

    def __str__(self):
        return self.projectName


class Contact(models.Model):
    subject = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=17)
    message = models.TextField()

    def __str__(self):
        return self.email

