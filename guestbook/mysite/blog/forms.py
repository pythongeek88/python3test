from django import forms
from .models import Blog

from django.template.defaultfilters import slugify


class PostForm(forms.ModelForm):
	class Meta:
		model = Blog
		fields = [
			'title',
			'body',
			'image',
			'category',
		]
'''class AddAdvertForm(ModelForm):
    region = forms.ModelChoiceField(queryset=Russian_Federation_Regions.objects.order_by('region'))
    city = forms.Field(widget=forms.Select)
    category = forms.ModelChoiceField(queryset=CategoryAdvert.objects.order_by('name'))
    title = forms.CharField()
    description = forms.CharField(widget=forms.Textarea)
    phone_number = forms.CharField(widget=forms.NumberInput)

    class Meta:
        model = Advert
        fields = '__all__'	'''