from django import forms

class SearchForm(forms.Form):
    query = forms.CharField(label ='Search for tweets containing:', max_length=70)