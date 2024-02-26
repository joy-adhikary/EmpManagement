from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Admin
from rest_framework import status
from .serializer import AdminSerializers


@api_view(['GET', 'POST'])
def admIndex(request):
    if request.method == 'GET':
        Admin = {
            "Type": "Admin",
            'Name': 'Joy Adhikary',
            "email": "admin@gmail.com",
            "password": "1234567890",
            'Request type': request.method,
        }
        print("Yho, you hit Get method from admin")

        # Getting queryParameter From url
        query = request.GET.get('q')

        print('Query Data is ==>', query)
        return Response({'Admin': Admin, 'Requested Query': query})

    elif request.method == 'POST':

        # getting put data from front end
        post_content = request.data

        print("Yho, you heat Post method from admin")
        print(post_content)
        return Response(post_content)

    else:
        return Response({"message": "Method not allowed"}, status=405)

#  standard methods to CRUD datas


@api_view(['GET', 'POST', 'PUT', 'PATCH'])

def admStdIndex(request):
    if request.method == 'GET':
        data = Admin.objects.all()
        print("all data", data)
        serialized_data = AdminSerializers(data, many=True)
        return Response(serialized_data.data)


    elif request.method == 'POST':
        post_content = request.data
        print("Post content =>", post_content)
        serialized_data = AdminSerializers(data=post_content)
        if serialized_data.is_valid():
            # save to database
            serialized_data.save()
            return Response(serialized_data.data, status=status.HTTP_201_CREATED)

        return Response({"Message": serialized_data.errors}, status=status.HTTP_406_NOT_ACCEPTABLE)
        # return Response(serialized_data.errors)


    elif request.method == 'PUT':
        Put_content = request.data
        print("PUT content =>", Put_content)
        # id = Put_content['id']
        serialized_data = AdminSerializers(data = Put_content)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data)

        return Response({"Message": serialized_data.errors}, status=status.HTTP_406_NOT_ACCEPTABLE)


    elif request.method == "PATCH":
        patch_content = request.data
        print("PATCH content =>", patch_content)
        serialized_data = AdminSerializers(data=patch_content, partial=True)
        print("PATCH info ", patch_content)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data)

        return Response({"Message": serialized_data.errors}, status=status.HTTP_406_NOT_ACCEPTABLE)
