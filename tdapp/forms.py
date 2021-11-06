from django import forms
from django.forms import ModelForm
from .models import *

class RecordsForm(forms.ModelForm):
    class Meta:    
        model = Records 
        fields = '__all__' 