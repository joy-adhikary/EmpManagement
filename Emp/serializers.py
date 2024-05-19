
from rest_framework import serializers
from .models import Emp

from django.contrib.auth.models import User

# Convert queryset ( database info ) to json format or vise-varsa 

class EMPSerializers(serializers.ModelSerializer):

#  Kon model ke serialize korbo seita ei meta te bole dite hobe 
    class Meta:
        model = Emp
        # show some selected fields
        # fields = ['password', 'username','email']

        # show all fileds 
        fields = '__all__'
        
        # Exclude only name fields . mane amr kase 100 ta model fields ashe, tar majhe ami just name ta show korbo nah.
        # exclude= ['user_type']



class EMPSerializers2(serializers.ModelSerializer):

    class Meta:
        model = Emp
        fields = ['user_type','username']
    

class RegisterSerializers(serializers.Serializer):

    username = serializers.CharField()
    password = serializers.CharField()
    email = serializers.EmailField()

    def validate(self, request):

        # check if User already exists or not 
        if request['username']:
            if User.objects.filter(username=request['username']).exists():
                raise serializers.ValidationError({'Massage': 'Ops!!! User already exists'})


        # check if Email already exists or not   
        if request['email']:
            if User.objects.filter(email=request['email']).exists():
                raise serializers.ValidationError({'Massage': 'Ops!!! Email already exists'})
            
        return request
    
    def create(self, validated_data):
        
        print("validated Data :" ,validated_data)

        user = User.objects.create(
            username = validated_data['username'],
            email = validated_data['email'])
        user.set_password(validated_data['password'])

        return validated_data
            


