from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status
from .models import Emp
from .serializers import EMPSerializers, RegisterSerializers

from django.contrib.auth.models import User


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def empStdIndex(request):
    if request.method == 'GET':
        data = Emp.objects.all()
        # as we getting a query set or python obj
        serializer = EMPSerializers(data, many=True)
        return Response(serializer.data)
    

    elif request.method == 'POST':
        newData= request.data
        # convert json to python obj
        serializer = EMPSerializers(data=newData)
        # cheking  is it valid or not  
        if serializer.is_valid():
            # saving it to the database
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)

        return Response(serializer.errors)
    
    elif request.method == 'PUT':
        put_content = request.data
        old_data = EMPSerializers.objects.get(id = put_content['id'])
        # update existing data
        serialized_data = EMPSerializers(old_data,data = put_content)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response({"massege" : "Data Updated Sucessfully"}, status=status.HTTP_200_OK)
        
        return Response({"Message": serialized_data.errors}, status=status.HTTP_406_NOT_ACCEPTABLE)
    
    else:
        deleted_id= request.data['id']
        deleted_data = Emp.objects.get(id=deleted_id)
        deleted_data.delete()
        return Response({"msg": " Data has been deleted"}, status=status.HTTP_200_OK)
        


class empApiviewClass(APIView):
    
    def get(self, request):
        return Response({"msg": "This is get test"})
    
    def post(self, request):
        return Response({"msg": "This is post test"})
    
    def put(self, request):
        return Response({"msg": "This is put test"})
    
    def delete(self, request):
        return Response({"msg": "This is delete test"})


class RegisterUser(APIView):
    def post(self, request):
        data = request.data 
        registerSerializer = RegisterSerializers(data = data)

        # if data are not correctly provide 
        if not registerSerializer.is_valid():
            return Response({
                'status': False,
                'message': registerSerializer.errors
            }, status.HTTP_400_BAD_REQUEST)
        
        registerSerializer.save()

        return Response({
            'status': True,
            'message': 'User Registered Successfully',
            'data': registerSerializer.data,
            }, status.HTTP_201_CREATED)
        
