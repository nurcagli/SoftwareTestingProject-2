# forms.py
from django import forms

# class RegisterForm(forms.Form):
#     email = forms.EmailField(max_length=100)
#     password = forms.CharField(widget=forms.PasswordInput)
#     agree = forms.BooleanField(required=True)

from .models import Industry
from .models import Blog

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'image', 'content']


class IndustryForm(forms.ModelForm):
    class Meta:
        model = Industry
        fields = ['title', 'desc', 'content', 'image' ]
        widgets = {
            'desc': forms.Textarea(attrs={'rows': 3}),  # Çoklu satır metin alanı için
            'content': forms.Textarea(attrs={'rows': 10}),  # Çoklu satır metin alanı için
        }


