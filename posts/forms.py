from django import forms
from .models import Post, Rate


class PostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Post
        fields = ['title', 'choices', 'description', 'image']


class RateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(RateForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Rate
        fields = ['rating']

