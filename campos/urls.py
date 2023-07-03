from django.urls import path

from .views import MateriaView, home

urlpatterns = [
    path('<slug:slug>', MateriaView.as_view(), name='materia'), # new
    #path('', HomeView.as_view(), name='home'),
    path('',home, name="home"),
]