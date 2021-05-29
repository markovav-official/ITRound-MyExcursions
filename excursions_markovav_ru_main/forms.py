from django import forms


class PassLoginForm(forms.Form):
    username = forms.CharField(
        max_length=32,
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Имя пользователя',
            }
        )
    )
    password = forms.CharField(
        max_length=64,
        required=False,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Пароль',
            }
        )
    )
