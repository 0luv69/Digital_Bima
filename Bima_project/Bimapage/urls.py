from django.urls import path, include
from Bimapage.views import *

urlpatterns = [
    path('', homepage, name="home"),
    path('appoinment/',appoinment, name='appoinment'),
    path('signup/', register, name="register"),
    path('login/', login_page, name="login"),
    path('logout/', logout_page, name="logout"),

]