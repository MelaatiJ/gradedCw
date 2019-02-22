from django.shortcuts import render

# Create your views here.

#functions that connect to my webpages
def index(request, name):
    return render(request, 'icApp/index.html')


def base(request, name):
    return render(request, 'icApp/details.html')



def about(request, name):
    return render(request, 'icApp/details.html')



