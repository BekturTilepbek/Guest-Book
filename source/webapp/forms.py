from django import forms
from django.forms import widgets

from webapp.models import Entry


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['name', 'email', 'text']
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
            'email': widgets.EmailInput(attrs={'class': 'form-control', 'placeholder': 'example@gmail.com'}),
            'text': widgets.Textarea(attrs={'class': 'form-control', 'cols': 50, 'rows': 5})
        }


class SearchForm(forms.Form):
    query = forms.CharField(
        widget=widgets.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Имя автора',
            }),
    )


class DeleteEntryForm(forms.Form):
    email = forms.EmailField(
        required=True,
        label='Введите email автора',
        widget=widgets.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'example@gmail.com'
            }
        ),
        error_messages={
            'required': 'Заполните это поле'
        },
    )

    def __init__(self, *args, **kwargs):
        self.author_email = kwargs.pop('author_email')
        super(DeleteEntryForm, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")

        if self.author_email and email:
            if self.author_email != email:
                self.add_error('email', "Введенный email должен совпадать с email автора!")

        return cleaned_data
