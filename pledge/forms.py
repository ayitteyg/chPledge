from django import forms 
from .models import *
from. resources import *
from django.contrib.auth.models import User



class DateInput(forms.DateInput):
    input_type = 'date'
        


class loginform(forms.Form):
    username = forms.CharField(max_length=30, label='',widget=forms.TextInput (attrs={'placeholder': 'username'}))
    password = forms.CharField(label=(""), widget=forms.PasswordInput (attrs={'placeholder': 'password'}))
    def clean(self):
        cleaned_data = super(loginform, self).clean()
        return cleaned_data 


class receiptform(forms.Form):
    date = forms.DateField(label='',widget= DateInput())
    amount = forms.FloatField(label='',widget=forms.TextInput (attrs={'placeholder': 'GHc: 0.00'}))
    def clean(self):
        cleaned_data = super(receiptform, self).clean()
        return cleaned_data 


class Pledgeform(forms.ModelForm):
    class Meta:
        model = Pledges
        fields = ("name","pamount", "option", "pdate", "fdate")
        labels = {'name':'Member Name',
                  'option': 'payment option',
                  'pamount':'Pledge amount',
                  'pdate':'date pledging',
                  'fdate': 'when to finish payment'}
        widgets = {
            'pdate': DateInput(),
            'fdate': DateInput(),
        }
    def clean(self):
        cleaned_data = super(Pledgeform, self).clean()
        return cleaned_data




class Registerform(forms.ModelForm):
    class Meta:
        model = Register
        fields = ("name","contact")
    def clean(self):
        cleaned_data = super(Registerform, self).clean()
        return cleaned_data







#HADLING FILES AND DOWNLOADS #
files = (("Registered Members","Registered Members"),
         ("Receipt Records","Receipt Records"),
         ("Members Contact","Members Contact"),
         ("Members Pledges","Members Pledges"),
         ("Members payments","Members payments"),
         ("Members balances","Members balances"),
         
         )

class exportFileform(forms.Form):
    report = forms.ChoiceField(choices=files)
    def clean(self):
        cleaned_data = super(exportFileform, self).clean()
        return cleaned_data 
