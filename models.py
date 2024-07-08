from django.db import models
# Create your models here.
class Home(models.Model):
    sno = models.AutoField(primary_key = True)
    title = models.CharField(max_length = 200)
    content = models.TextField()
    slug = models.CharField(max_length = 100)
    time = models.DateTimeField(auto_now_add = True)
    image = models.ImageField(upload_to="Home/images",default="")
    def __str__(self):
        return self.title

class Mentalhealth(models.Model):
    sno = models.AutoField(primary_key = True)
    title = models.CharField(max_length = 200)
    content = models.TextField()
    slug = models.CharField(max_length = 100)
    time = models.DateTimeField(auto_now_add = True)
    image = models.ImageField(upload_to="Mentalhealth/images", default="")
    def __str__(self):
        return self.title

class Heartdiseases(models.Model):
    sno = models.AutoField(primary_key = True)
    title = models.CharField(max_length = 200)
    content = models.TextField()
    slug = models.CharField(max_length = 100)
    time = models.DateTimeField(auto_now_add = True)
    image = models.ImageField(upload_to="Heartdiseases/images", default="")
    def __str__(self):
        return self.title

class Covid(models.Model):
    sno = models.AutoField(primary_key = True)
    title = models.CharField(max_length = 200)
    content = models.TextField()
    slug = models.CharField(max_length = 100)
    time = models.DateTimeField(auto_now_add = True)
    image = models.ImageField(upload_to="Covid/images", default="")
    def __str__(self):
        return self.title

class Immunization(models.Model):
    sno = models.AutoField(primary_key = True)
    title = models.CharField(max_length = 200)
    content = models.TextField()
    slug = models.CharField(max_length = 100)
    time = models.DateTimeField(auto_now_add = True)
    image = models.ImageField(upload_to="Immunization/images", default="")
    def __str__(self):
        return self.title
class Contact(models.Model):
    sno = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 40)
    email = models.CharField(max_length = 40)
    time = models.DateTimeField(auto_now_add=True)

