from django.shortcuts import render
from .forms import PersonFrm
# Create your views here.
def person_list(request):
    return render(request,"person/person_list.html")
def person_form(request):
    form = PersonFrm
    return render(request,"person/person_form.html",{'form':form})
def person_delete(request):
    return 
