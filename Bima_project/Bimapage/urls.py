from django.urls import path, include
from Bimapage.views import *

urlpatterns = [
    path('', homepage, name="home"),
    path('documentation/', documentation, name="documentation"),
    path('appoinment/',appoinment, name='appoinment'),
    path('medicalstore/', med_login, name="med_login"),
    path('add-med/', add_medicine, name="add_med"),


    path('signup/', register, name="register"),
    path('login/', login_page, name="login"),
    path('logout/', logout_page, name="logout"),

]