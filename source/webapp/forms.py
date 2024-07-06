from django import forms
from django.forms import widgets

from webapp.models import Entry


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['name', 'email', 'text', 'status']
        error_messages = {
            'name': {
                'required': 'Заполните поле'
            },
            'email': {
                'required': 'Заполните поле',
            },
            'text': {
                'required': 'Заполните поле'
            }
        }

        widgets = {
            'name': widgets.TextInput(attrs={'class': 'form-control'}),
            'email': widgets.EmailInput(attrs={'class': 'form-control'}),
            'text': widgets.Textarea(attrs={'class': 'form-control', 'cols': 50, 'rows': 5})
        }


class SearchForm(forms.Form):
    query = forms.CharField(widget=widgets.TextInput(attrs={'class': 'form-control'}))

    widgets = {
        'query': widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'Имя автора'}),
    }