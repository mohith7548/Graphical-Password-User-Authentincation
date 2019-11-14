from django.urls import path, include
from .views import home_page, register_page, login_page, logout_page, login_from_uid

urlpatterns = [
    path('', home_page, name='home'),
    path('register/', register_page, name='register'),
    path('login/', login_page, name='login'),
    path('login/<str:uid>', login_from_uid, name='login_uid'),
    path('logout/', logout_page, name='logout'),
]
