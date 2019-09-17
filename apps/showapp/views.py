from django.shortcuts import render, HttpResponse, redirect
from .models import Show
from django.contrib import messages


def root(request):
    return redirect("/shows")
def index(request):
    context = {
    	"all_Shows": Show.objects.all(),
    }
    return render(request, "showapp/index.html", context)

def DisplayShow(request, num):
    context = {
    	"show": Show.objects.get(id=num),
    }
    return render(request, "showapp/index4.html", context)

def newShow(request):
    if request.method == "POST":
        errors = Show.objects.basic_validator(request.POST)
            # check if the errors dictionary has anything in it
        if len(errors) > 0:
            # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
            for key, value in errors.items():
                messages.error(request, value)
            # redirect the user back to the form to fix the errors
            return render(request, "showapp/index2.html")
        else:
            t=request.POST["title"]
            nw=request.POST["network"]
            des=request.POST["desc"]
            RD=request.POST["RDate"]
            sh=Show.objects.create(title=t,network=nw, desc= des,RDate=RD)
            sh.save()
            return redirect(f'/shows/{sh.id}' )
    return render(request, "showapp/index2.html")

def editShow(request, num):
    if request.method == "POST":
        errors = Show.objects.basic_validator(request.POST)
            # check if the errors dictionary has anything in it
        if len(errors) > 0:
            # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
            for key, value in errors.items():
                messages.error(request, value)
            # redirect the user back to the form to fix the errors
            return redirect(f'/shows/{num}/edit' , messages)
        else:
            t=request.POST["title"]
            nw=request.POST["network"]
            des=request.POST["desc"]
            # des=request.POST.get("desc","No description")
            RD=request.POST["RDate"]
            sh=Show.objects.get(id=num)
            sh.title=t
            sh.network=nw
            sh.desc=des
            sh.RDate=RD
            sh.save()
            return redirect(f'/shows/{sh.id}')
    context = {
    	"show": Show.objects.get(id=num),
    }
    return render(request, "showapp/index3.html", context)

def destroy(request,num):
    sh = Show.objects.get(id=num)	
    sh.delete()
    return redirect("/shows")