from django import forms
from .models import SuccessPost

class SuccessPostForm(forms.ModelForm):
    class Meta:
        model = SuccessPost
        fields = ['content', 'image']
