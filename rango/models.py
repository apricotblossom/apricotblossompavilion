from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    yturl = models.URLField()
    cats = models.CharField(max_length=128)
    name = models.CharField(max_length=128, unique=True)
    releasedate = models.DateField(blank=True)
    introduction = models.CharField(max_length=1024)
    review = models.CharField(max_length=1024)
    iosurl = models.URLField()
    andurl = models.URLField()
    pcurl = models.URLField()
    pictureurl = models.CharField(max_length=128)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    slug = models.SlugField(blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category,self).save(*args,**kwargs)

    class Meta: 
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Page(models.Model):
    category = models.ForeignKey(Category)
    message = models.CharField(max_length=1024)
    evaluation = models.IntegerField(default=0)
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.message


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    age = models.IntegerField(default=0)
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):
        return self.user.username

