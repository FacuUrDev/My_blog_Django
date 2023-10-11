from django import forms
from .models import Comment
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
#Se crea un formulario para los comentarios
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')
        
# Apply summernote to specific fields.
class SomeForm(forms.Form):
    foo = forms.CharField(widget=SummernoteWidget())  # instead of forms.Textarea