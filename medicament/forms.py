from django.forms import ModelForm
from medicament.models import Comment
from django import forms

class CommentForm(ModelForm):
    class Meta:
        model = Comment       #help me
        fields = ['text']
      
# тест загрузки данных из локального файла!
class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()  