from django.urls import path
from .import views



#url paths that all connect to the home page
urlpatterns=[
    path('home/', views.index, name="index"),
    path('home/base/', views.base, name='base'),
    path("home/about/", views.about, name="about"),
]

