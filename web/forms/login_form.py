from django import forms

class LoginForm(forms.Form):
  username = forms.CharField(max_length=100)
  password = forms.CharField(widget=forms.PasswordInput())  
  #persist = forms.CheckboxInput()


from django import forms

class CreateLoginForm(forms.Form):
  firstName = forms.CharField(max_length=100)
  lastName = forms.CharField(max_length=100)
  username = forms.CharField(max_length=100)
  password = forms.CharField(widget=forms.PasswordInput())
  password_again = forms.CharField(widget=forms.PasswordInput())
  #persist = forms.CheckboxInput()
