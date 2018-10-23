from django import forms

class EntryForm(forms.Form):
    entry_form = forms.CharField(label="How ya doin'?")
