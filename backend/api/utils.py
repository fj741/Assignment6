from django.core.mail import send_mail
from django.conf import settings
from rest_framework.request import Request

def order_confirmed_email(order_id, user_email):
    subject = 'Thank You For Placing Your Order'
    message = f"Your order number is {order_id}"
    send_mail(subject, message, 'gamehq738@gmail.com', [user_email])

def temp():
    subject = "Yes"
    message = "It works"
    send_mail(subject, message, 'gamehq738@gmail.com', ["farrelljack741@gmail.com"])    
    
 
