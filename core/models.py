from django.db import models

class Deinosti(models.Model):
    title = models.CharField(max_length=90)
    description = models.TextField()

class Step(models.Model):
    image = models.FileField()
    title = models.CharField(max_length=50)
    description = models.TextField()

class Gallery(models.Model):
    url = models.FileField()

class Certificate(models.Model):
    title = models.CharField(max_length=80)
    url = models.FileField()

class Phase(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    ref = models.CharField(max_length=20, default="foo")
    btn_text = models.CharField(max_length=30, default="bar")
    image = models.FileField()

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    image = models.FileField()

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.email
