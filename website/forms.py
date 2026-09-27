from django import forms

class SampleForm(forms.Form):
    button = forms.HiddenInput()