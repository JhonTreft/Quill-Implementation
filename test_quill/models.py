from django.db import models

from django_quill.fields import QuillField

# Create your models here.
#
#


class EditorModel(models.Model):
    content = QuillField()
