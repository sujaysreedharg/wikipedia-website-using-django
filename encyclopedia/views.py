from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from markdown2 import Markdown
from django.urls import reverse
from random import randint



from . import util
markdowner=Markdown()
def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def create(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        if title == "" or content == "":
            return render(request, "encyclopedia/error.html", {"message": "Enter Data To Proceed.", "title": title, "content": content})
        if title in util.list_entries():
            return render(request, "encyclopedia/error.html", {"message": "Title already exists. Try another.", "title": title, "content": content})
        util.save_entry(title, content)
        return HttpResponseRedirect(reverse("index"))
    return render(request, "encyclopedia/create.html")
    
def title(request,title):
    global content
    content = util.get_entry(title)
    if content is None:
        return render(request,"encyclopedia/error.html",{ "message" : "ERROR! No Such Page"
        })
    else:
        return render(request, "encyclopedia/getpage.html",{
    
        "title" : title.capitalize(), "content" : markdowner.convert(content)
        })
def edit(request,title):
    content = util.get_entry(title)
    if request.method == "POST":
        content = request.POST.get("content")
        if content == " ":
            return render(request, "encyclopedia/edit.html", {"message": "Enter Content to proceed.", "title": title, "content": content})
        util.save_entry(title, content)
        return redirect("entry", title=title)
    return render(request, "encyclopedia/edit.html", {'content': content, 'title': title})
def randompage(request):
    index=util.list_entries()
    random_title = index[randint(0, len(index)-1)]
    return redirect("entry", title=random_title)
      
def search(request):
    q = request.GET.get('q')
    entries=util.list_entries()   
    if q not in util.list_entries():
        return render(request, "encyclopedia/search.html", { "q": q,"entries": entries})
    else:
        return redirect("entry",title=q)





    
