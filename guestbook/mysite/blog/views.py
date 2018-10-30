from django.shortcuts import render
from django.contrib import messages
# Create your views here.
from django.http import HttpResponseRedirect
from .models import Blog, Category
from .forms import PostForm
from django.shortcuts import render_to_response, get_object_or_404

def index(request):
	return render_to_response('index.html', {
		'categories': Category.objects.all(),
		'posts': Blog.objects.all()[:10]
	})

def view_post(request, slug):
	return render_to_response('view_post.html', {
		'post': get_object_or_404(Blog, slug=slug)
	})

def view_category(request, slug):
	category = get_object_or_404(Category, slug=slug)
	return render_to_response('view_category.html', {
		'category': category,
	'posts': Blog.objects.filter(category=category)[:10]
	})

def view_create_post(request):
	form = PostForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, 'Successfully Created')
		return render_to_response('view_post.html', {
			'post': get_object_or_404(Blog, slug=instance.slug)
		})
	context = {
	'form': form,
	}
	return render(request, 'form.html', context)
