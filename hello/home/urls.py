from django.contrib import admin
from django.urls import path
from home import views

#-----------------------

admin.site.site_header = "Kitshaar Admin"
admin.site.site_title = "Site Admin Portal"
admin.site.index_title = "Welcome to Site Adminstrator Portal"


# ----------------------

urlpatterns = [
    path("", views.index, name="home"),
    path("about", views.about, name="about"),
    path("contact", views.contact, name="contact"),
]
