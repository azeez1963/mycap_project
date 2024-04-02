from rest_framework import serializers, exceptions
from .models import Category, Product, Store
from django.contrib.auth.models import User

class CategorySerializer(serializers.Serializer):
      id=serializers.IntegerField(read_only=True)
      name=serializers.CharField(max_length=50, min_length=4)


      def validate(self, attrs):
            name=attrs.get('name')
            if name == 'drinks':
                  raise exceptions.ValidationError("please drinks is not accepted category")
            return attrs

      def create(self, validated_data):
            return Category.objects.create(name=validated_data['name'])

      def update(self, instance, validated_data):
            instance.name=validated_data.get('name', instance.name)
            instance.save()
            return instance
      
class CreateProductSerializer(serializers.ModelSerializer):
      class Meta:
            model=Product
            fields=['product_name', 'description', 'price', 'discount_price', 'category', 'expire_date', 'production_date', 'rating']
      

class ProductSerializer(serializers.ModelSerializer):
      class Meta:
            model=Product
            fields=['id', 'product_name', 'description', 'price', 'discount_price', 'category','expire_date']


class UserCreateSerializer(serializers.ModelSerializer):
      password=serializers.CharField(max_length=68, min_length=3, write_only=True)
      password2=serializers.CharField(max_length=68, min_length=3, write_only=True)
      class Meta:
            model=User
            fields=['username', 'email', 'password', 'password2']


      def validate(self, attrs):
            username = attrs.get('username')
            
            # Check if a user with the provided username already exists
            users = User.objects.filter(username=username)
            if users.exists():
                  raise exceptions.ValidationError('A user with this username already exists.')
            elif users.count() > 1:
                  raise exceptions.ValidationError('Multiple users with the same username exist. This is a server error. Please contact support.')
            
            password1 = attrs.get('password')
            password2 = attrs.get('password2')
            if password1 != password2:
                  raise exceptions.ValidationError('Passwords do not match.')
            
            return attrs
      
      def create(self, validated_data):

            return User.objects.create_user(username=validated_data['username'], email=validated_data['email'], password=validated_data['password'])
      
      
class StoreSerializer(serializers.ModelSerializer):
      class Meta:
            model=Store
            fields=['name', 'location']

class CreateStoreSerializer(serializers.ModelSerializer):
      class Meta:
            model=Store
            fields=['name', 'location']