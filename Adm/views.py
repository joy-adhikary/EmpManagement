from rest_framework.response import Response
from rest_framework.decorators import api_view


# Create your views here.

@api_view(['GET','POST'])

def index(request):
    if request.method == 'GET':
        Admin={
            "Type":"Admin",
            'Name': 'Joy Adhikary',
            "email":"admin@gmail.com",
            "password":"1234567890",
            'Request type': request.method,
        }
        print("Yho, you heat Get method from admin")
        return Response(Admin)
    elif request.method=='POST':
        Admin={
            "Type":"Admin",
            'Name': 'Joy Adhikary',
            "Email":"admin@gmail.com",
            "Password":"1234567890",
            'Request type': request.method,
        }
        print("Yho, you heat Post method from admin")
        return Response(Admin)

    else:
        return Response({"message": "Method not allowed"}, status=405)