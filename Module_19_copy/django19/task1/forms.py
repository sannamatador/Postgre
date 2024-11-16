from django import forms


class UserRegister(forms.Form):
    username = forms.CharField(max_length=30, label="Введите имя")
    password = forms.CharField(min_length=8, label="Введите пароль")
    password1 = forms.CharField(min_length=8, label="Повторите пароль")
    age = forms.IntegerField(max_value=110, label='Введите свой возраст')
    registration = forms.BooleanField(required=False, label="Зарегистрироваться")

    def __str__(self):
        return self.title


