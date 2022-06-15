from django.shortcuts import redirect, render
from .forms import SearchMap,AddRomania, AddCountry
from .search import  searchMap, addMap

def search(response):
    data=""
    if response.method=="POST":
        search_form=SearchMap(response.POST)
        if search_form.is_valid():
            data = searchMap(search_form.cleaned_data["start"],search_form.cleaned_data["goal"]) 
    else:
        search_form=SearchMap()
    return render(response,'main/search.html', {"search_form":search_form, "data":data})
 
 
def addRomania(response):
    data=""
    if response.method=="POST":
        mapData=AddRomania(response.POST)
        if mapData.is_valid():
            data = addMap(mapData.cleaned_data["distance"],mapData.cleaned_data["straight_line"])       
    else:
        mapData=AddRomania()
    return render(response,'main/addRomania.html', {"mapData":mapData,"data":data})

def addCountry(response):
    data=""
    if response.method=="POST":
        mapData=AddCountry(response.POST)
        if mapData.is_valid():
            data = addMap(mapData.cleaned_data["distance"],mapData.cleaned_data["straight_line"])       
    else:
        mapData=AddCountry()
    return render(response,'main/addCountry.html', {"mapData":mapData,"data":data})
