from djongo.models import CharField, Model, DecimalField, EmailField, BooleanField
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib.auth.hashers import make_password
from djongo import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    picture = models.ImageField(default="no_image_attached")
    name = CharField(max_length=100)
    price = DecimalField(max_digits=10, decimal_places=2)
    type_choices = [
        ('Game','Game'),
        ('Accessory','Accessory'),
        ('Console', 'Console')
    ]
    console_choices = [
        ('PS4', 'PS4'),
        ('XBOX ONE', 'XBOX ONE'),
        ('NINTENDO SWITCH','NINTENDO SWITCH'),
        ('PS5', 'PS5'),
        ('XBOX SERIES X', 'XBOX SERIES X'),
    ]
    type = models.CharField(max_length=50, choices=type_choices)
    console = models.CharField(max_length=50, choices=console_choices)
    
    def __str__(self):
        return self.name

class UserManager(BaseUserManager):
    def create_user(self, email, fname, lname, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, fname=fname, lname=lname, **extra_fields)

        user.set_password(password)
        user.save(using=self.db)
        return user
    def create_superuser(self, email, fname, lname, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(email, fname, lname, password, **extra_fields)
        
class User(AbstractBaseUser, PermissionsMixin):
    fname = models.CharField(verbose_name="First Name",  max_length=50)        
    lname = models.CharField(verbose_name="Last Name",  max_length=50)
    email = models.EmailField(verbose_name="Email",unique=True)
    date_joined = models.DateTimeField(_('date_joined'), default=timezone.now)
    is_active = models.BooleanField(_('active'), default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager() 
     
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['fname', 'lname']
    
    
    def first_name(self):
        return self.fname
    
    def full_name(self):
        return f"{self.fname} {self.lname}"
    
    def __str__(self):
        return self.email

class Order(Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_number = models.CharField(max_length= 40)
    created = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.order_number