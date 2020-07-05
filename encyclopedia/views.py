from django.shortcuts import render
from django.http import HttpResponse
from . import util
import markdown
import random
md = markdown.Markdown()
fn=[]
test=[]
def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })
def entry(request, title):
    if util.get_entry(title)==None:
        return render(request,"encyclopedia/error.html")
    else:

        return HttpResponse(md.convert(util.get_entry(title)))

def search(request):
    name1=request.GET.get("q")
    
    fn=[]
   
    if util.get_entry(name1)==None:
        ent=util.list_entries()
       
        
        for e in ent:
           
           
           str1=str(name1).lower()
           str2=str(e).lower()
           if(str2.find(str1)!=-1):
                
                fn.append(e)
                
        if len(fn)==0:
             return render(request,"encyclopedia/error.html")
        else:
             return render(request, "encyclopedia/index.html", {
           "fn": fn,"entries": util.list_entries(),"vv":"=>Are you searching for any of these pages?"})

    else:

        return HttpResponse(md.convert(util.get_entry(name1)))

def create(request):
   
    return render(request,"encyclopedia/create.html")
def save(request):
    tt=request.GET.get("title1")
    tx=request.GET.get("texts")

    test= util.list_entries()
   
    if tt in test:
        return render(request,"encyclopedia/error1.html")
    else:
       
        util.save_entry(tt, tx)
        return HttpResponse(md.convert(util.get_entry(tt)))


def edit(request,nm1):
     ko=nm1
     return render(request,"encyclopedia/edit.html",{"txt":util.get_entry(ko)})
def saveedit(request):
    op=request.GET.get("ko")
    ed=request.GET.get("textsed")
    
    util.save_entry(op, ed)
    
    return HttpResponse(md.convert(util.get_entry(op)))
def randomp(request):
    rn=[]
    rn=util.list_entries()
    j=len(rn)
    h=random.randint(0,j-1)
    return HttpResponse(md.convert(util.get_entry(rn[h])))


    


