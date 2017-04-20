from django import forms
from django.forms.widgets import Textarea,RadioSelect
from mainapp.models import Profile


class NewPost(forms.ModelForm):
    class Meta:
        model = Profile
        fields =[
            "name",
            "job",
            # "timestamp"
        ]
        labels = {
            'name': 'Name',
            'Job': 'Your Job'
        }


        help_texts = {
            'name' : 'Enter your full name'
        }

        error_messages = {
            'name': {
                'max_length': "This title is too long.",
            },
        }


        # widgets = {
        #     'content': Textarea(attrs={'cols': 80, 'rows': 10,'class':'tinymce'}),
        #     'status' : RadioSelect,
        #     'writer' : forms.HiddenInput(),
        #     # 'timestamp': forms.HiddenInput(),
        # }

class LoginForm(forms.Form):
    username = forms.EmailField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    remember = forms.BooleanField(label="Remember Me",required=False )


class SignUpForm(forms.Form):
    firstname = forms.CharField(max_length=100)
    lastname = forms.CharField(max_length=100)
    username = forms.EmailField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)