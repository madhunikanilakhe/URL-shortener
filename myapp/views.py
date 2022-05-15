from urllib import request
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import LongToShort

# Create your views here.
def hello_world(request):
    return HttpResponse("hello world")

def home_page(request):
    context = {
        "submitted": False,
        "error":False
    }

    if request.method == 'POST':
        

        data = request.POST                 # dict
        long_url = data['longurl']
        custom_name = data['custom_name']

        # print(long_url)
        # print(custom_name)
        #create
        try:
            # CREATE
            obj = LongToShort(long_url = long_url, short_url = custom_name)
            obj.save()

            # READ
            date = obj.date
            clicks = obj.clicks

            context["long_url"] = long_url
            context["short_url"] = request.build_absolute_uri() + custom_name
            context["date"] = date
            context["clicks"] = clicks
            context["submitted"] = True

        except:
            context["error"] = True


    # else:
    #     print("User not sending anything")    

    return render(request, "index.html", context)

def redirect_url(request,short_url):
    row=LongToShort.objects.filter(short_url=short_url)
    print(row)
    if len(row)==0:
        return HttpResponse("No such short url exists")
    
    obj=row[0]

    long_url=obj.long_url
    obj.clicks=obj.clicks+1
    obj.save()
    print(long_url)
    return redirect(long_url)

def task(request):

    context = {
        "my_name": "John",
        "x": 15
    }
    return render(request, "test.html", context)

def all_analytics(request):
    rows=LongToShort.objects.all()
    context={
        "rows":rows
    }

    return render(request,"all-analytics.html",context)

