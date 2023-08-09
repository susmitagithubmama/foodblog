from django import forms

class StudentReg(forms.Form):
    name = forms.CharField(max_length=30)
    email = forms.EmailField()
    phone = forms.IntegerField()
    dob = forms.DateField()
    password = forms.CharField(widget=forms.PasswordInput)
    options = (('option1','male'),('option2','female'),('option3','others'))
    subjects = (('sub1','Math'),('sub2','Eng'),('sub3','sci'))
    # gender = forms.ChoiceField(choices=options)
    gender = forms.ChoiceField(choices=options,widget=forms.RadioSelect)
    subject = forms.MultipleChoiceField(choices=subjects,widget=forms.CheckboxSelectMultiple)

    # resetPassword = forms.PasswordInput() 
