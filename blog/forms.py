from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'author', 'image')
        widgets = {
            'image': forms.FileInput(),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['author'].widget.attrs['readonly'] = True

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']

class EditCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
