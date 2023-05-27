from django.urls import path
from gt.views import *
app_name='something'
urlpatterns=[
    path('hardik/',hardik,name='hardik'),
]