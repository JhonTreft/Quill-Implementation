from django.contrib import admin

from .models import *

# Register your models here.
#
#
#

@admin.register(EditorModel)

class EditorAdmin(admin.ModelAdmin):
    pass
