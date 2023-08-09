from django import forms

class MyForm(forms.Form):
    sname = forms.CharField(max_length=10,min_length=4,error_messages={'required':'Dont leave this field empty','max_length':'10 characters only','min_length':'5 characters minimum'})
    spass = forms.CharField(widget=forms.PasswordInput,max_length=50)
    semail = forms.EmailField()

class BlogForm(forms.Form):
    title = forms.CharField(max_length=20,min_length=10,error_messages={'required':'Dont leave this field empty','max_length':'20 characters only','min_length':'10 characters minimum'})
    author = forms.CharField(max_length=20)
    post = forms.CharField(widget=forms.Textarea)