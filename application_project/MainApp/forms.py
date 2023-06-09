from django import forms
from .models import Places


class AddPost(forms.ModelForm):
    class Meta:
        model = Places
        fields = ('place_name', 'comment')
        widgets = {
            'place_name': forms.TextInput(attrs={'class': 'place_name', 'placeholder': 'Название места'}),
            'comment': forms.Textarea(attrs={'class': 'comment', 'placeholder': 'Расскажи об этом'})
        }
