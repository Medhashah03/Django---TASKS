from django import forms


class Formss(forms.Form):
    name = forms.CharField(label="name", max_length=70)
    
