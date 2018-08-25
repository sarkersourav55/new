from django import forms
from .models import todo

class todoform(forms.Form):
    text=forms.CharField(max_length=40)
    
class newform(forms.ModelForm):
    class Meta :
        model=todo
        fields=['text']


     