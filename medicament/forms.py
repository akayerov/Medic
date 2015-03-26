from django.forms import ModelForm
from medicament.models import Comment

class CommentForm(ModelForm):
    class Meta:
        model = Comment       #help me
        fields = ['text']
        