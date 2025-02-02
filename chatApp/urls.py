from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('<str:room>/',views.room),
    path('checkroom',views.checkroom),
    path('send',views.send),
    path("getMessages/<str:room>/",views.getMessages)
]