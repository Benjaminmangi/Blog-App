from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
            'tags': forms.TextInput(attrs={'class': 'form-control', 'data-role': 'tagsinput'}),
        }
        help_texts = {
            'content': 'You can use Markdown syntax to format your post.',
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        } 