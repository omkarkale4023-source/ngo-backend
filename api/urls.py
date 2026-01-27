from django.urls import path
from .views import ContactView, DonationView, LoginActivityView

urlpatterns = [
    path("contact/", ContactView.as_view()),
    path("donate/", DonationView.as_view()),
    path("login/", LoginActivityView.as_view()),
]
