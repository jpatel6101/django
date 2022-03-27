from django import forms


class PersonForm(forms.Form):
    firstname = forms.CharField(max_length=40, required=True,
                                 widget = forms.TextInput(attrs={'class': 'form-control'}))
    lastname = forms.CharField(max_length=40, required=True,
                                widget = forms.TextInput(attrs={'class': 'form-control'}))
    fage = forms.IntegerField(min_value=1, max_value=150, required=True,
                             widget = forms.TextInput(attrs={'class': 'form-control'}))