from django.contrib.auth.forms import (
    UserChangeForm,
)
from django import forms
from users.models import User


class CustomUserCreationForm(forms.ModelForm):
    password1 = forms.CharField(help_text='Введіть пароль', label='', widget=forms.PasswordInput, error_messages={'required': ''})
    password2 = forms.CharField(help_text='Введіть пароль ще раз', label='',  widget=forms.PasswordInput, error_messages={'required': ''})
    email = forms.EmailField(help_text='Вкажіть вашу електронну пошту', label='',
                             error_messages={'required': ''})
    first_name = forms.CharField(help_text='Вкажіть ваше імя', label='',  error_messages={'required': ''})
    last_name = forms.CharField(help_text='Вкажіть ваше прізвище', label='',  error_messages={'required': ''})
    number_tel = forms.CharField(help_text='Вкажіть ваш мобільний номер', label='',
                                 error_messages={'required': ''})
    use_required_attribute = False

    class Meta:
        use_required_attribute = False
        model = User
        fields = ('email', 'first_name', 'last_name', 'number_tel', 'password1', 'password2')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Паролі не збігаються!")
        return password2

    def save(self, commit=True):
        user = super(CustomUserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'number_tel')
