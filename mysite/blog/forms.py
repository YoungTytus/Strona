from django import forms
from .models import Post, Category

# choices = [('coding', 'coding'), ('crypto', 'crypto')]
choices = Category.objects.all().values_list('name', 'name')


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'author', 'category', 'body', 'snippet')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control fomr-sml', 'placeholder': 'Tytuł'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control fomr-sml', 'placeholder': 'Tag'}),
            'author': forms.Select(attrs={'class': 'form-control fomr-sml'}),
            'category': forms.Select(choices=choices, attrs={'class': 'form-control fomr-sml'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'snippet': forms.TextInput(attrs={'class': 'form-control fomr-sml'})
        }


class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'category', 'body', 'snippet')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control fomr-sml', 'placeholder': 'Tytuł'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control fomr-sml', 'placeholder': 'Tag'}),
            'category': forms.Select(choices=choices, attrs={'class': 'form-control fomr-sml'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'snippet': forms.TextInput(attrs={'class': 'form-control fomr-sml'})
        }
