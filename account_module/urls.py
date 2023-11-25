from django.urls import path
from . import views

urlpatterns = [

    path('',views.RegisterView.as_view(),name='login_register'),
    path('login',views.login_req,name='login'),
    path('logout',views.log_out,name='logout'),
    path('dashboard',views.dsahboard.as_view(),name='dashboard'),

]
