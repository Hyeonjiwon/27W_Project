from django import forms
from .models import Community
 
class CommunityFormModel(forms.ModelForm):
    class Meta:
        model = Community
 
        fields = [
            'title', 
            'user',
            'text', 
            'image', 
            'category',
            ] 