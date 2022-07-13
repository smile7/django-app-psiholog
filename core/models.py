from django.db import models
# Create your models here.

""" class Recipe(models.Model):
    DIFFICULTY_LEVELS = (
        ('Easy', 'Easy'),
        ('Medium', 'Medium'),
        ('Hard', 'Hard'),
    )
    name = models.CharField(max_length=120)
    ingredients = models.CharField(max_length=400)
    picture = models.FileField()
    difficulty = models.CharField(choices=DIFFICULTY_LEVELS, max_length=10)
    prep_time = models.PositiveIntegerField()
    prep_guide = models.TextField()

    def __str_(self):
        return "Recipe for {}".format(self.name) """


class Deinosti(models.Model):
    title = models.CharField(max_length=90)
    description = models.TextField()

class Step(models.Model):
    image = models.FileField()
    title = models.CharField(max_length=50)
    description = models.TextField()

class Gallery(models.Model):
    image = models.FileField()

class Certificate(models.Model):
    title = models.CharField(max_length=80)
    image = models.FileField()

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


""" class Blogadmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on')
    list_filter = ("status", )
    search_fields = ['title', 'content']
    # prepopulating slug from title
    prepopulated_fields = {'slug': ('title', )}
    summernote_fields = ('content', )
    image = models.FileField()
 """