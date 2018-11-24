from django import forms

#Entry Form is a basic form object with a CharField
#used for writing a journal entry
class EntryForm(forms.Form):
    entry_form = forms.CharField(label="How ya doin'?")
