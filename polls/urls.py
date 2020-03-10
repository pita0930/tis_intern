from django.urls import path

from . import views

urlpatterns = [

    path('', views.index, name='index'),
    path('event/', views.event, name='event'),
    path('makeevent/', views.event_new, name='event_new'),
    path('mypage/', views.my_page, name='my_page'),
    path('talk/', views.talk1, name='talk1'),
]
