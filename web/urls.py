"""
Definition of urls for CompanyPyWeb.
"""


from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index')
]
