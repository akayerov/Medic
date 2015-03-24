from django.forms import ModelForm
from medicament.models import Comment

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        