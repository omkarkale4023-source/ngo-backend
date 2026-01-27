from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt

from .models import Contact, Donation, LoginActivity
from .serializers import (
    ContactSerializer,
    DonationSerializer,
    LoginActivitySerializer
)

# ---------------- CONTACT ----------------
@csrf_exempt
@api_view(["POST"])
def contact_api(request):
    serializer = ContactSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Contact saved"}, status=201)
    return Response(serializer.errors, status=400)


# ---------------- DONATION ----------------
@csrf_exempt
@api_view(["POST"])
def donation_api(request):
    serializer = DonationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Donation saved"}, status=201)
    return Response(serializer.errors, status=400)


# ---------------- LOGIN ----------------
@csrf_exempt
@api_view(["POST"])
def login_api(request):
    serializer = LoginActivitySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Login activity saved"}, status=201)
    return Response(serializer.errors, status=400)
