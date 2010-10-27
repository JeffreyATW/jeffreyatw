from django import forms
from jeffreyatw.portfolio.models import Entry

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry

    def __init__(self, *args, **kwargs):
        super(EntryForm, self).__init__(*args, **kwargs)
        self.fields['description'].widget.attrs['class'] += " mceEditor"
