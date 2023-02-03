from django.shortcuts import render
from django.http import HttpResponse


#These are the functions that are created to send an http response.
#Request is a static variable with the request itself - it does not contain any usable data (as far as I know).
#The second variable is one in which can be returned. The words are the extentions that are input onto the url.
def projects(request):
    return render(request, 'projects.html')
def project(request):
    return render(request, 'project.html')
def strproject(request, words):
    return HttpResponse(f'You have successfully reached the strprojects page! using {words} as an ID.')