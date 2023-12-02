from rest_framework.response import Response
from rest_framework.decorators import api_view


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
        print("Yho, you heat Get method from EMP")
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