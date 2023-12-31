from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Emp
from .serializers import EMPSerializers


# Normal way

@api_view(['GET', 'POST'])
def Empindex(request):
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
        EMP = {
            "Type": "EMP",
            'Name': 'Joy Adhikary',
            'Deg': 'Soft. Eng',
            "Email": "EMP@gmail.com",
            "Password": "1234567890",
            'Request type': request.method,
        }
        print("Yho, you heat Post method from EMP")
        return Response(EMP)

    else:
        return Response({"message": "Method not allowed"}, status=405)


# Using serializers

@api_view(['GET', 'POST'])
def EmIndexWithSerializer(request):
    if request.method == 'GET':
        data = Emp.objects.all()
        # as we getting a query set 
        serializer = EMPSerializers(data, many=True)
        return Response(serializer.data)
    

    elif request.method == 'POST':
        newData= request.data
        # convert json to python obj
        serializer = EMPSerializers(data=newData)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,"your data submitted")

        return Response(serializer.errors)

