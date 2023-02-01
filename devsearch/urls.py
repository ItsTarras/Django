"""devsearch URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from django.http import HttpResponse


#These are the functions that are created to send an http response.
#Request is a static variable with nothing. Don't use it as an actual variable.
#The second variable within the functions are required to be the string that is sent via the paths.
def projects(request):
    return HttpResponse(f'You are on the {request} page.')
def project(request):
    return HttpResponse(f'You are on the project (no s) page.')
def strproject(request, words):
    return HttpResponse(f'You have successfully reached the strprojects page! using {words} as an ID')


#These are the url additives that will navigate to a different page.
#The first variable is the addition to the url,
#The second variable is the function it is calling,
#The third variable is the name of the variable being called.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('projects/', projects, name="projects (Custom typed)"),
    path('project/', project, name="Singular project"),
    path('strproject/<str:words>', strproject, name="String used")
]
