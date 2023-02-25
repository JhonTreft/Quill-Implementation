from django_quill.forms import QuillFormField

from django import forms


class EditorForm(forms.Form):
    body= QuillFormField()



