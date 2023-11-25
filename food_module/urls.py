from django.urls import path
from . import views

urlpatterns = [

    path('', views.Home_page.as_view(),name='home_page'),
    path('reserv', views.reserv, name='reservation'),
    path('comment', views.comments, name='add_comments'),
    path('like<int:pk>', views.like_part, name='like'),
]
