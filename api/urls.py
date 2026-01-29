from django.urls import path
from .views import contact_view, donate_view, login_view

urlpatterns = [
    path("contact/", contact_view),
    path("donate/", donate_view),
    path("login/", login_view),
]
