from django.shortcuts import render

# Create your views here.
def person_list(request):
    return render(request,"person/person_list.html")
def person_form(request):
    return render(request,"person/person_form.html")
def person_delete(request):
    return 
