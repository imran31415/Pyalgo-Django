#files.py
import re
from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.forms.extras.widgets import SelectDateWidget

class CodeForm(forms.Form):
    name_field = 'test algorithm'
    code = forms.CharField(label ='code', widget=forms.Textarea(attrs={'rows':30,'cols':100}))