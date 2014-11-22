from django import forms
from crispy_forms.helper import FormHelper
from .import models


class UserForm(forms.Form):
    name = forms.CharField(label='A very long name',
                           max_length=5)
    money = forms.IntegerField(label='Money')

    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.label_class = 'col-lg-2'
    helper.field_class = 'col-lg-8'

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)


class UserForm2(forms.ModelForm):
    class Meta:
        model = models.User
