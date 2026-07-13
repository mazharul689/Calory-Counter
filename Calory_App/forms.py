from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import *

class RegisterForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ['username', 'email', 'password1', 'password2']

    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for i_name, i in self.fields.items():
            i.widget.attrs['class']='form-control'

class AuthForm(AuthenticationForm):
    class Meta:
        model = UserModel
        fields = ['username','password']

    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for i_name, i in self.fields.items():
            i.widget.attrs['class']='form-control'

class PProfileForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = '__all__'
        exclude = ['user','bmr']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for i_name, i in self.fields.items():
            i.widget.attrs['class']='form-control'

class CaloryConsumptionForm(forms.ModelForm):
    class Meta:
        model = CaloryConsumptionModel
        fields = '__all__'
        exclude = ['user']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for i_name, i in self.fields.items():
            i.widget.attrs['class']='form-control'