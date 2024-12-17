from collections import namedtuple

from django.urls import path
from . import views
urlpatterns=[
    path("about/",views.about,name='about'),
    path("booking/",views.booking,name="booking"),
    path("contact/",views.contact,name="contact"),
    path("home/",views.home,name="home"),
    path("menu/",views.menu,name="menu"),
    path("form/",views.form,name="form")
]