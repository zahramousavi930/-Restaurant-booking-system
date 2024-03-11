from django.urls import path
from . import views
from .views import robots_txt
urlpatterns = [

    path('', views.Home_page.as_view(),name='home_page'),
    path('comment', views.comments, name='add_comments'),
    path('like', views.like_part, name='like'),
    path('BookTable', views.Book_table.as_view(), name='book_table'),
    path('about-us', views.about_us.as_view(), name='about_us'),
    path('robots.txt', robots_txt, name='robots_txt'),
]


