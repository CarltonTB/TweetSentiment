from django import forms

class SearchForm(forms.Form):
    query = forms.CharField(label ='Search for tweets containing:', max_length=70)
    
class ClassifyForm(forms.Form):
    text = forms.CharField(label = 'Enter some text to classify:',widget=forms.Textarea, max_length=140)