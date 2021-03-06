from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

from taggit.managers import TaggableManager

import markdown
# Create your models here.


STATUS = (
    ('1', 'Active'),
    ('0', 'Inactive'),
)


class Article(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    body_markdown = models.TextField()
    blog_file = models.FileField(upload_to='images', blank=True)
    created_by = models.ForeignKey(User)
    pub_date = models.DateTimeField('date published')
    slug = models.SlugField(max_length=255)
    tags = TaggableManager()

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.body = markdown.markdown(self.body_markdown)
        self.slug = slugify(self.title)
        super(Article, self).save(*args, **kwargs)


class Comment(models.Model):
    blog = models.ForeignKey(Article)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=1, choices=STATUS, default=0)

    def __unicode__(self):
        return self.name
