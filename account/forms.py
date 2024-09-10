from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


#Classe modèle
class InscriptionForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'class':'form-control',
            'placeholder':'Enter Your E-mail',
        })
    )
    first_name = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your Last Name',
        }),
        label = "Last Name"
    )

    last_name = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your First Name',
        })
       ,
       label = "First Name"
    )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2']
        #Stylisation des champs
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your User Name',
                'autofocus': 'autofocus'
            }),
            'password1': forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Password',
                 'style': 'position: absolute; left: 15px;',
            }),
            'password2': forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your password again',
            }),
        }

        labels = {
            
            'email': 'Email',
            'username': 'User Name',
            'password1': 'Password',
            'password2': 'Password again',
        }

    # Validation de l'email de l'utilisateur
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is alredy exist.")
        return email
 

#Class forgot password      
class ForgotForm(forms.ModelForm):
   email = forms.EmailField()
   

class NewPassword(forms.ModelForm):
   password1 = forms.CharField(max_length=100,min_length=5)
   password2 = forms.CharField(max_length=100,min_length=5)
   