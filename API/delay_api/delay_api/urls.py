"""delay_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
import time
from django.http.response import HttpResponse
from django.urls import path


def delay_view(request):
    seconds = int(request.GET.get('seconds', '0'))

    print(f"Request received. I'm waiting for {seconds} secs")
    time.sleep(seconds)
    print("Done waiting!")

    return HttpResponse(f"Done, I waited for {seconds} secs")

urlpatterns = [
    path('delay-me', delay_view)
]
