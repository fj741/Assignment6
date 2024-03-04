from rest_framework import serializers
from .models import User, Product

class UserSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only = True)
    class Meta:
        model = User
        fields = ['id','fname','lname','email','password', 'confirm_password']
        
    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError("Passwords do not match")
        if User.objects.filter(email=data['email']).exists():
            raise serializers.ValidationError("Email already exists")
        
        return data
    
    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user
    
class ProductSerializer(serializers.ModelSerializer):
    picture = serializers.ImageField(required=False)
    class Meta:
        model = Product
        fields = ['id', 'picture', 'name', 'price', 'type', 'console']
        
        