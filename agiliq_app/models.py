from django.db import models
from taggit.managers import TaggableManager
# Create your models here.


STATUS = (
    ('1', 'Active'),
    ('0', 'Inactive'), 
)


class Article(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    blog_file = models.FileField(upload_to='images', blank=True)
    created_by = models.CharField(max_length=100)
    pub_date = models.DateTimeField('date published')
    tags = TaggableManager()

    def __unicode__(self):
        return self.title


class Comment(models.Model):
    blogid = models.ForeignKey(Article)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    dessription = models.TextField()
    status = models.CharField(max_length=1, choices=STATUS, default=0)

    def __unicode__(self):
        return self.name
