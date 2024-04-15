from django import forms
from django.core import validators


class PhoneField(forms.CharField):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.validators.append(validators.RegexValidator(
            regex=r'^\d{10}$',
            message=('Введите корректный номер из 10 цифр'),
            code='invalid_phone'
        ))
class ClientForm(forms.Form):
    name = forms.CharField(max_length=100, label='Имя Фамилия',
                           widget=forms.TextInput(attrs={'required': 'True'}))
    password = forms.CharField(max_length=128, label='Пароль', widget=forms.PasswordInput)
    confirm_password = forms.CharField(max_length=128, label='Подтверждение пароля',
                                       widget=forms.PasswordInput)
    email = forms.EmailField(label='email')
    phone = PhoneField(label='Номер телефона')
    address = forms.CharField(max_length=200, label='Домашний адрес')

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        if password != confirm_password:
            raise forms.ValidationError("Пароли не совпадают. Попробуйте еще раз.")

        return cleaned_data