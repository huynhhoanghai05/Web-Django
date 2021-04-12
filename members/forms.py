from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms

class SignUpFrom(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control' }))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control' }))

    class Meta:
        model = User
        fields = ("username", "first_name","last_name","email","password1", "password2")
        
    def __init__(self, **kwargs):
        super(SignUpFrom,self).__init__(**kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'

class EditProfileForm(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control' }))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control' }))
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control' }))
    last_login = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control' }))
    is_supperuser = forms.CharField(max_length=100, widget=forms.CheckboxInput(attrs={'class':'form-check' }))
    is_staff = forms.CharField(max_length=100, widget=forms.CheckboxInput(attrs={'class':'form-check' }))
    is_active = forms.CharField(max_length=100, widget=forms.CheckboxInput(attrs={'class':'form-check' }))
    date_joined = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control' }))

    class Meta:
        model = User
        fields = ("username", "first_name","last_name","email","password","last_login","is_supperuser","is_staff","is_active","date_joined")
        

# class PasswordChangingForm(PasswordChangeForm):
#     email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
#     first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control' }))
#     last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control' }))

#     class Meta:
#         model = User
#         fields = ("username", "first_name","last_name","email","password1", "password2")
        
