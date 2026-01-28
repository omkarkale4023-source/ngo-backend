from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Contact, Donation, LoginActivity
from .serializers import ContactSerializer, DonationSerializer, LoginActivitySerializer


class ContactView(APIView):
    def post(self, request):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Contact saved"}, status=201)
        return Response(serializer.errors, status=400)


class DonationView(APIView):
    def post(self, request):
        serializer = DonationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Donation saved"}, status=201)
        return Response(serializer.errors, status=400)


class LoginActivityView(APIView):
    def post(self, request):
        serializer = LoginActivitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Login activity saved"}, status=201)
        return Response(serializer.errors, status=400)
