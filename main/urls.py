from django.urls import path
from main import views

urlpatterns = [
    path('', views.index, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name= 'login' ),
    path('logout/', views.logout, name= 'logout' ),
    path('plist/', views.plist, name= 'plist' ),
    path('pdetail/', views.pdetail, name= 'pdetail' ),
    path('sr/', views.search, name= 'search' ),
]
