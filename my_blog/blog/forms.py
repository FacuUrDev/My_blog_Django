  
from django import forms
from .models import Comment
#Se crea un formulario para los comentarios
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')