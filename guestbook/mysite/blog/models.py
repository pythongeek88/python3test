from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify


# Create your models here.

class Blog(models.Model):
	title = models.CharField(max_length=100, unique=True)
	slug = models.SlugField(('slug'), max_length=100, unique=True, blank=True)
	body = models.TextField()
	image = models.FileField(null=True, blank=True)
	posted = models.DateTimeField(db_index=True, auto_now_add=True)
	category = models.ForeignKey('blog.Category', None)
	
	def save(self,  *args, **kwargs):
		self.slug = slugify(self.title)
		return super(Blog, self).save(*args, **kwargs)
	
	def __unicode__(self):
		return '%s' % self.title
	def __str__(self):
		return '%s' % self.title

	def get_absolute_url(self):
		return reverse('view_blog_post', args=(self.slug,))
	class Meta:
		ordering = ['-posted']

class Category(models.Model):
	title = models.CharField(max_length=100, db_index=True)
	slug = models.SlugField(max_length=100, db_index=True)

	def __unicode__(self):
		return '%s' % self.title
	def __str__(self):
		return '%s' % self.title

	def get_absolute_url(self):
		return reverse('view_blog_category', args=(self.slug,))