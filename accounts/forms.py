from django import forms
from django.contrib.auth import authenticate, get_user_model

User = get_user_model()
class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("This user does not exist")
        return super(UserLoginForm, self).clean(*args, **kwargs)


class Register(forms.ModelForm):
    email= forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    email2=forms.EmailField(label="Confirm Email")
    class Meta:
        model=User
        fields=["username","email","email2","password"]

    def clean_email2(self):
        email=self.cleaned_data.get("email")
        email2=self.cleaned_data.get("email2")
        if email != email2:
            raise forms.ValidationError("email must match")
        email_qs=User.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError("already registered")
        return email