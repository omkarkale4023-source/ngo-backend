from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ContactSerializer, DonationSerializer, LoginSerializer

@api_view(["POST"])
def contact_view(request):
    serializer = ContactSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Contact saved"})
    return Response(serializer.errors, status=400)


@api_view(["POST"])
def donate_view(request):
    serializer = DonationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Donation saved"})
    return Response(serializer.errors, status=400)


@api_view(["POST"])
def login_view(request):
    serializer = LoginSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Login saved"})
    return Response(serializer.errors, status=400)
