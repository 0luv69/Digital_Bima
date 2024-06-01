from django.urls import path, include
from Bimapage.views import *

urlpatterns = [
    path('', homepage, name="home"),

]