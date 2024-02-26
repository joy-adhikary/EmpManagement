from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Emp
from .serializers import EMPSerializers


# Normal way

@api_view(['GET', 'POST'])
def empIndex(request):
    if request.method == 'GET':
        EMP = {
            "Type": "Employee",
            'Name': 'Joy Adhikary',
            'Deg': 'Soft. Eng',
            "email": "Emp@gmail.com",
            "password": "1234567890",
            'Request type': request.method,
        }
        print("Yho, you hit Get method from EMP")
        return Response(EMP)

    elif request.method == 'POST':
        post_content = request.data
        print(post_content)
        print("Yho, you hit Post method from EMP")
        return Response({'Posted Content':post_content})

    else:
        return Response({"message": "Method not allowed"}, status=405)


# Using serializers

@api_view(['GET', 'POST'])
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

