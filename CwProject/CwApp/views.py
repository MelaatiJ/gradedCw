from django.shortcuts import render

# Create your views here.

#functions that connect to my webpages
def index(request):
    return render(request, 'CwApp/index.html')


def base(request):
    return render(request, 'CwApp/base.html')



def about(request):
    return render(request, 'CwApp/about.html')



