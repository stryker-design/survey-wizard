from http.client import MULTIPLE_CHOICES
from django import forms
from .models import Survey, Question, Option
from crispy_forms.helper import FormHelper


class SurveyForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
            super(SurveyForm, self).__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.helper.form_show_labels = False 

    class Meta:
        model =  Survey
        fields = ['title']


class QuestionForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
            super(QuestionForm, self).__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.helper.form_show_labels = False 
            
    class Meta:
        model = Question
        fields = ['prompt', 'type']

    
class OptionForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
            super(OptionForm, self).__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.helper.form_show_labels = False 

    class Meta:
        model = Option
        fields = ["text"]

# class CommentBoxForm(forms.ModelForm):
#     def __init__(self, *args, **kwargs):
#             super(OptionForm, self).__init__(*args, **kwargs)
#             self.helper = FormHelper()
#             self.helper.form_show_labels = False 
    
#     class Meta:
#         model = CommentBox
#         fields = ['comment']


class AnswerForm(forms.Form):
    def __init__(self, *args, **kwargs):
        options = kwargs.pop("options")
        # Options must be a list of Option objects
        choices = {(o.pk, o.text) for o in options}
        super().__init__(*args, **kwargs)
        option_field = forms.ChoiceField(choices=choices, widget=forms.RadioSelect, required=True)
        self.fields["option"] = option_field

class BaseAnswerFormSet(forms.BaseFormSet):
    def get_form_kwargs(self, index):
        kwargs = super().get_form_kwargs(index)
        kwargs["options"] = kwargs["options"][index]
        return kwargs