from django import forms
from order.models import Order


class OrderForm(forms.ModelForm):
    email = forms.EmailField(help_text='Вкажіть вашу електронну пошту', label='Електронна пошта',
                             error_messages={'required': ''})
    first_name = forms.CharField(help_text='Вкажіть ваше імя', label='Імя', error_messages={'required': ''})
    last_name = forms.CharField(help_text='Вкажіть ваше прізвище', label='Прізвище', error_messages={'required': ''})
    number_tel = forms.CharField(help_text='Вкажіть ваш мобільний номер', label='Номер телефону', error_messages={'required': ''})
    address = forms.CharField(help_text='Вкажіть вашу адресу проживання, наприклад : "Мазепи 42"', label='Адреса',
                              error_messages={'required': ''})

    class Meta:
        model = Order
        fields = ['email', 'first_name', 'last_name', 'number_tel', 'address']
