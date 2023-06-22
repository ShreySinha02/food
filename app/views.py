from django.shortcuts import render
from django.http import HttpResponse
from .models import  Restaurants
# Create your views here.
def resrurants(request):
    search_field=''
    if request.method =='POST':
        search_field=str(request.POST.get('food'))

    datas = Restaurants.objects.all()
    datas=list(datas)
    detail=datas[0:20]
    if search_field != '':
        detail=[]
        for i in range(len(datas)):
            data=datas[i].items
            s=str(data)
            if s.lower().find(search_field)>0:
                detail.append(datas[i])
    return render(request,'index.html',{'data':detail})

def resturants_detail(request,id):
    data=Restaurants.objects.get(id=id)
    return render(request,'res.html',{'data':data,'dict':data.items.items()})
