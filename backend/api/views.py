"import stripe"
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework import status, generics
from rest_framework.views import APIView
from .utils import temp
from .serializers import ProductSerializer, UserSerializer
from .models import Product
from django.core.mail import send_mail
from django.conf import settings

@api_view(['GET'])
def home(request):
    return Response({"message":"Home Page"})

@api_view(['GET'])
def temp_email(request):
    temp()
    return Response({"message": "Email Sent"})

@api_view(['POST'])
def newsletter(request):
    if request.method == "POST":
        email = request.data.get('email')
        if email:
            subject = "Thank You For Subscribing To Our Newsletter"
            message = "Stay tuned for some exclusive offers"   
            send_mail(subject, message, 'gamehq738@gmail.com', [email]) 
            return Response({"message": "Email Sent"}, status=status.HTTP_200_OK)
        else:
            return Response({"message": "Email Could Not Be Sent"}, status=status.HTTP_400_BAD_REQUEST)
   
class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
class UserRegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login(request):
    email = request.data.get('email')
    password = request.data.get('password')

    user = authenticate(email=email, password=password)

    if user:
        return Response(status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_401_UNAUTHORIZED)
    
"""stripe.api_key = settings.STRIPE_SECRET_KEY
def checkout(request):
    amount = 49999
    payment_intent = stripe.PaymentIntent.create(
        amount=amount,
        currency='euro',
        payment_method_types=['card'],
    )"""
@api_view(['GET'])
def error_page(request):
    return Response({"message": "404 Page"}, status=status.HTTP_404_NOT_FOUND)
