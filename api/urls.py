from django.urls import path
from .views import contact_api, donation_api, login_api

urlpatterns = [
    path("contact/", contact_api),
    path("donate/", donation_api),
    path("login/", login_api),
]
