from django.shortcuts import render
from imageapp.models import Catogory,Image 

def Home(request):
    cats= Catogory.objects.all()
    images=Image.objects.all()
    data={'images': images, 'cats':cats}
    return render(request,'home.html',data)


def ShowCategory(request,cid):
    cats=Catogory.objects.all()
    category= Catogory.objects.get(pk=cid)
    images=Image.objects.filter(cat=category)
    
    data={'images': images, 'cats':cats}
    return render(request,'home.html',data)


def Searchbar(request):
    
    if request.method=='GET':
        search=request.GET.get('search')
        search=Image.objects.filter(description=search)
        context={'search':search}
   # search=Image.objects.get(description=search)
        return render(request,'home.html',context)