from django.forms import ModelForm, widgets

from .models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ('text', 'group')
        widgets = {
            'text': widgets.Textarea(attrs={
                'class': 'form_control',
                'placeholder': 'Текст поста'
            })
        }
