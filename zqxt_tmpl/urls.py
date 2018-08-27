"""zqxt_tmpl URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from learn import views as learn_views
import django

urlpatterns = [
    url(r'^$',learn_views.home,name='home'),
    url(r'^admin/', admin.site.urls),
    url(r'^addUser/',learn_views.addUser,name='addUser'),
    url(r'^addCoach/',learn_views.addCoach,name='addCoach'),
    url(r'^addPerson/',learn_views.addPerson,name='addPerson'),
    url(r'^loginCoach/',learn_views.loginCoach,name='loginCoach'),
    url(r'^loginPerson/',learn_views.loginPerson,name='loginPerson'),
    url(r'^check/',learn_views.check,name='check'),
    url(r'^check_result/',learn_views.check_result,name='check_result'),
    url(r'^adjust/',learn_views.adjust,name='adjust'),
    url(r'^adjust_result/(\d+)',learn_views.adjust_result,name='adjust_result'),
    url(r'^booking/',learn_views.booking,name='booking'),
    url(r'^booking_result/',learn_views.booking_result,name='booking_result'),
    url(r'^book_result/',learn_views.book_result,name='book_result'),
    url(r'^bus/',learn_views.bus,name='bus'),
    url(r'^bus_result/(\d+)',learn_views.bus_result,name='bus_result'),    
    url(r'^cancal/',learn_views.cancal,name='cancal'),

]
