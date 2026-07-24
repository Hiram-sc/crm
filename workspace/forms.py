import re

from django import forms
from .models import Contact
from django.core.exceptions import ValidationError


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone', 'occupation']

        error_messages = {
            'name': {
                'required': 'Preencha este campo.' 
                },
            'email': {
                'required': 'E-mail é obrigatório.',
                'invalid': 'E-mail inválido.', 
                'unique': 'E-mail já existente.' 
                },
            'phone': {
                'required': 'Preencha este campo.' 
                },
            'occupation': {
                'required': 'Preencha este campo.' 
                }
        }

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-input'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-input',
                'placeholder': 'example@email.com'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': '(00) 00000-0000'
            }),
            'occupation': forms.TextInput(attrs={
                'class': 'form-input',
            })
        }

    def clean_name(self):
        name = (self.cleaned_data.get('name') or '').strip()

        if len(name.split()) < 2:
            raise ValidationError(
                'Deve conter nome e sobrenome.'
            )

        return name

    def clean_email(self):
        email = (self.cleaned_data.get('email') or '').strip().lower()

        return email

    def clean_phone(self):
        phone = (self.cleaned_data.get('phone') or '').strip()

        correct_phone = re.sub(r'\D', '', phone)

        if len(correct_phone) < 10 or len(correct_phone) > 11:
            raise ValidationError(
                'O número deve conter 10 dígitos e estar no formato (00) 00000-0000.'
            )

        if len(correct_phone) == 11 and correct_phone[2] != '9':
            raise ValidationError(
                'Número de telefone inválido.'
            )

        if correct_phone == correct_phone[0] * len(correct_phone):
            raise ValidationError(
                'Número de telefone inválido.'
            )

        return correct_phone