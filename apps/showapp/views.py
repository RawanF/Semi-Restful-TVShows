from django.shortcuts import render, HttpResponse, redirect
from .models import Show

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
        t=request.POST["title"]
        nw=request.POST["network"]
        des=request.POST["description"]
        RD=request.POST["RDate"]
        sh=Show.objects.create(title=t,network=nw, desc= des,RDate=RD)
        sh.save()
        return redirect(f'/shows/{sh.id}' )
    return render(request, "showapp/index2.html")

def editShow(request, num):
    if request.method == "POST":
        t=request.POST["title"]
        nw=request.POST["network"]
        des=request.POST["description"]
        RD=request.POST["RDate"]
        sh=Show.objects.get(id=num)
        sh.title=t
        sh.network=nw
        sh.desc=des
        sh.RDate=RD
        sh.save()
        return redirect(f'/shows/{sh.id}' )
    context = {
    	"show": Show.objects.get(id=num),
    }
    return render(request, "showapp/index3.html", context)

def destroy(request,num):
    sh = Show.objects.get(id=num)	
    sh.delete()
    return redirect("/shows")