from django.db import models

# Create your models here.
class Skill(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    select = models.BooleanField()
    icon = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.title

class Project(models.Model):
    name = models.CharField(max_length=20)
    content = models.CharField(max_length=50)
    link = models.URLField(max_length=500, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

class Section(models.Model):
    title = models.CharField(max_length=20)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class About(models.Model):
    name = models.CharField(max_length=20)
    position = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    website = models.URLField()
    introduction = models.TextField()

    def __str__(self):
        return self.name

class Education(models.Model):
    name = models.CharField(max_length=50)
    major = models.CharField(max_length=50)
    time = models.CharField(max_length=50)
    link = models.URLField()

    def __str__(self):
        return self.major

class WorkExperience(models.Model):
    name = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    time = models.CharField(max_length=50)
    introduction = models.TextField()


    def __str__(self):
        return self.name