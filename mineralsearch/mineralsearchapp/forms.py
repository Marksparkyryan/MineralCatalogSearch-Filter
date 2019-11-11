from django import forms

class MineralSearchForm(forms.Form):
    q = forms.CharField(max_length=48)
    