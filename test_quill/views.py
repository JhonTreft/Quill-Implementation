from django.shortcuts import render
from .models import *


# Create your views here.
#
#
#
#
#


from .form import EditorForm

def Home(request):
    model = EditorModel.objects.all()
    form= EditorForm()
    context={
            'editor':model,
            'form':form,
            }
    return render(request,'home.html',context)


def Add(request):
    if request.method == 'POST': # If the form has been submitted...
        form = EditorForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules passprint
            print(form.cleaned_data['body'])
        modelo = EditorModel.objects.create(content=form.cleaned_data['body'])
    
    return render(request,"home.html")
