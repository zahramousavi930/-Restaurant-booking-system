from django.urls import path
from . import views

urlpatterns = [

    path('',views.RegisterView.as_view(),name='login_register'),
    path('login',views.login_req,name='login'),
    path('logout',views.log_out,name='logout'),
    path('edit-dashboard/<int:pk>',views.edit_dsahboard.as_view(),name='edit-dashboard'),
    path('dashboard',views.dsahboard.as_view(),name='dashboard'),
    path('activate-account/<email_active_code>', views.ActivateAccountView.as_view(), name='activate_account'),
    path('forget_pass', views.ForgetPasswordView.as_view(), name='forget_password_page'),
    path('reset_pass/<active_code>', views.ResetPasswordView.as_view(), name='reset_password_page'),
    path('add-to-order', views.add_product_to_order, name='add_product_to_order'),
    path('add-to-shopping_cart', views.shoping_cart.as_view(), name='shoping_cart'),

]
