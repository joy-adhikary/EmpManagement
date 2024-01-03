from rest_framework.response import Response
from rest_framework.decorators import api_view

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
        print("Yho, you hit Get method from admin")
        
        #Getting queryParameter From url
        query = request.GET.get('query')

        print('Query Data is ==>', query)
        return Response({'Admin': Admin, 'Requested Query': query })

    elif request.method=='POST':

        # getting put data from front end
        post_content = request.data

        print("Yho, you heat Post method from admin")
        print(post_content)
        return Response(post_content)

    else:
        return Response({"message": "Method not allowed"}, status=405)