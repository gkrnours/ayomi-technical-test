from django import forms

class SigninForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField()

    def save(self):
        print(self.cleaned_data)