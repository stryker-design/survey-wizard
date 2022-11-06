from django import forms
from core.models import Contact
from crispy_forms.helper import FormHelper


class ContactForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
            super(ContactForm, self).__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.helper.form_show_labels = False 

    class Meta:
        model = Contact
        fields = '__all__'
