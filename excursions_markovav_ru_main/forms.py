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


class AddExcursionForm(forms.Form):
    name = forms.CharField(
        max_length=32,
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control text-center',
                'placeholder': 'Название экскурсии',
            }
        )
    )
    datetime = forms.CharField(
        max_length=32,
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control text-center',
                'placeholder': 'Время и дата экскурсии (mm:hh DD.MM.YYYY)',
            }
        )
    )
    image_link = forms.CharField(
        max_length=10000,
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control text-center',
                'placeholder': 'Ссылка на изображение',
            }
        )
    )
    description = forms.CharField(
        max_length=10000,
        required=True,
        widget=forms.Textarea(
            attrs={
                'class': 'form-control text-center',
                'placeholder': 'Описание экскурсии',
            }
        )
    )
