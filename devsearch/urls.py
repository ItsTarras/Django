from django.contrib import admin
from django.urls import path, include



#These are the url additives that will navigate to a different page.
#The first variable is the addition to the url,
#The second variable is the function it is calling,
#The third variable is the name of the variable being called.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('projects.urls'))
]
