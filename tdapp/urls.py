from django.urls import path
from . import views

urlpatterns = [
    
    path('',views.home),
    path('home',views.home),
    path('add',views.add),
    path('edit/<str:x>',views.edit),
    path('update/<str:x>', views.update),
    path('erase/<str:x>', views.erase),
]