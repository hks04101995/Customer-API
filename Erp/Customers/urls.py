from django.conf.urls import url,include
from rest_framework import routers
from .views import CustomerView
route = routers.DefaultRouter()

route.register('Customer',CustomerView)

urlpatterns = [
    url('',include(route.urls)),
]
