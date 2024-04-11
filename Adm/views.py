from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Admin
from rest_framework import status
from .serializer import AdminSerializers

#  standard methods to CRUD datas

@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])

def admStdIndex(request):
    if request.method == 'GET':
        data = Admin.objects.all()
        # print("all data", data)
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

        updatedObj = Admin.objects.get(id= Put_content['id'])
        serialized_data = AdminSerializers(updatedObj,data = Put_content)

        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data)

        return Response({"Message": serialized_data.errors}, status=status.HTTP_406_NOT_ACCEPTABLE)


    # patch a pertial update kora jai.Baki data as it is rekhe dibe. just passed data gulai update kore dibe.

    elif request.method == "PATCH":
        patch_content = request.data
        print("PATCH content =>", patch_content)

        updatedObj = Admin.objects.get(id = patch_content['id'])
        serialized_data = AdminSerializers(updatedObj,data = patch_content, partial = True)
        print("Updated object", updatedObj)

        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data)

        return Response({"Message": serialized_data.errors}, status=status.HTTP_406_NOT_ACCEPTABLE)
    
    #  delete method 
    else:
        request_data = request.data 
        updatedObj = Admin.objects.get(id=request_data['id'])
        updatedObj.delete()
        return Response({"Message": "Entity deleted :)"}, status=status.HTTP_200_OK)
