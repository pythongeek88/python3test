from django.contrib import admin
from .models import Blog, Category

class BlogAdmin(admin.ModelAdmin):
	list_display= ('title','body','image','posted','category',)
	exclude = ['posted']
	prepopulated_fields = {'slug': ('title',)}

class CategoryAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('title',)}

admin.site.register(Blog, BlogAdmin)
admin.site.register(Category, CategoryAdmin)
