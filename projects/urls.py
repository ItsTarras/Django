from django.urls import path
from . import views

urlpatterns = [
    path('projects/', views.projects, name="projects (Custom typed)"),
    path('project/', views.project, name="Singular project"),
    path('strproject/<str:words>', views.strproject, name="String used"),
    path('', views.homepage, name="Homepage"),
    path('tarrascv', views.cvpage, name='cv')
]