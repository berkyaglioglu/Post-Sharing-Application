from django import forms
from .models import Post, Rate, Ingredients


class PostForm(forms.ModelForm):
    ingredients = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple, queryset=Ingredients.objects.all())

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Post
        fields = ['title', 'description', 'image', 'ingredients']


class RateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(RateForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Rate
        fields = ['score']

