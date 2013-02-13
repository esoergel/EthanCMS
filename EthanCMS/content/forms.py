from django import forms
from content.settings import PAGE_MODEL, EDITABLE_PAGE_FIELDS


class UploadFileForm(forms.Form):
    name = forms.CharField(max_length=50)
    file  = forms.FileField()
