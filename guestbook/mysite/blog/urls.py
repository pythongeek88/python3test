from django.conf.urls import url, include
from .views import index, view_post, view_category, view_create_post

urlpatterns = [
    url(r'^$', index),
    url(r'^blog/view/(?P<slug>[^\.]+).html', view_post, name='view_blog_post'),
    url(r'^blog/category/(?P<slug>[^\.]+).html', view_category, name='view_blog_category'),
    url(r'^blog/create', view_create_post),
]
