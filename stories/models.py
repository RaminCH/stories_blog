from django.contrib.auth.models import User
from django.db import models
from djrichtextfield.models import RichTextField

# Create your models here.

class AboutPage(models.Model):
    title = models.CharField(max_length=255, blank=False, null=True)
    description = models.TextField(blank=False, null=True)
    #logs

    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class NavLinks(models.Model):
    title = models.CharField(max_length=255, blank=False, null=False)
    url = models.CharField(max_length=20, blank=True)
    active = models.BooleanField(default=True)

    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Contact(models.Model):
    name = models.CharField(max_length = 30, blank=False, null = False)
    # email = models.EmailField('e-Poct',blank = False, null = False)
    email = models.EmailField(blank = False, null = False)
    subject = models.CharField(max_length = 60, blank=False, null = False)
    message = models.TextField(blank = False,null = False)
    #logs

    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class Story(models.Model):
    title = models.CharField(max_length=50, blank=False, null=True)
    created_at = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='stories', blank=False, null= True)
    description = models.TextField(blank=False)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='stories',null=True)# class Category-ni bura elave edirik etc. Category 'Lunch-in icine class Categoryde muxtelif lunch-lar elave edirik sonra Story-se elave edirik'
    updated_at = models.DateTimeField(auto_now = True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='stories', default=1) #default=1 default user owner of recipes
    view_count = models.PositiveIntegerField('View count', default=0) # checks how many ppl watched the story

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-created_at',)
        verbose_name = 'Hekaye'
        verbose_name_plural = 'Hekayeler'

class Category(models.Model):
    title = models.CharField(max_length=50, blank=False, null=True)
    image = models.ImageField(upload_to='categories')
    #logs
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    

class Recipe(models.Model):
    title = models.CharField(max_length=50, blank=False, null=True)
    created_at = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='recipes', blank=False, null= True)
    description = models.TextField(blank=False)
    long_description = RichTextField('long description')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='recipes',null=True)
    updated_at = models.DateTimeField(auto_now = True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipes', default=1)
    view_count = models.PositiveIntegerField('View count', default=0) # checks how many ppl watched the recipe

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-created_at',)
        verbose_name = 'Resept'
        verbose_name_plural = 'Reseptler'


class Comment(models.Model):
    user = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    comment = models.TextField('Comment',)
    recipe = models.ForeignKey(Recipe, related_name='comments', on_delete=models.CASCADE, null = True, blank = True)
    story = models.ForeignKey(Story, related_name='comments', on_delete=models.CASCADE, null = True, blank = True)
    reply_comment = models.ForeignKey('self', related_name = 'reply_comments', on_delete = models.CASCADE,null = True, blank = True)

#logs
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}" #return "{} {}".format(self.user.first_name, self.user.last_name) is equial to  f"{self.user.first_name} {self.user.last_name}"

    def get_user_full_name(self):
        return "{} {}".format(self.user.first_name, self.user.last_name)

    class Meta:
        ordering = ('create_at',)
        verbose_name = 'Rey'
        verbose_name_plural = 'Reyler'


class Subscriber(models.Model):
    email = models.EmailField(max_length=60)
    #logs
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email