from django.db.models import OuterRef
from django.db.models import Subquery
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .models import Admin
from Emp.models import LinkEmpWithAdmin
from rest_framework import status
from .serializer import AdminSerializers
from rest_framework import routers, serializers, viewsets



                                            #? Using api view decorator

@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])

def admStdIndex(request):
    if request.method == 'GET':

        #! **request.query_params.dict() eite pura query param kei as it is search kore, as a result jkno query e kaj korbe jodi data thake 
        if request.query_params:
            datas = Admin.objects.filter(**request.query_params.dict())
        else:
            datas = Admin.objects.all()

        # filter out emp null values using ( __isnull )
        datas = datas.filter(emp__isnull = False)

        # eitar maddhome ami onno aktam model theke subquery kore data ene ei model er field ke set kore dicchi.
        salary_subquery = LinkEmpWithAdmin.objects.filter(emp_id=OuterRef('id')).values('salary')[:1]
        datas = datas.annotate(salarys=Subquery(salary_subquery))

        for data in datas:
            data.salary= data.salarys

        serialized_data = AdminSerializers(datas, many=True)
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




                                            #? Using api view class 


class AdminClass(APIView):

    def get(self, request):
          #! **request.query_params.dict() eite pura query param kei as it is search kore, as a result jkno query e kaj korbe jodi data thake 
        if request.query_params:
            datas = Admin.objects.filter(**request.query_params.dict())
        else:
            datas = Admin.objects.all()

        # filter out emp null values using ( __isnull )
        datas = datas.filter(emp__isnull = False)

        # eitar maddhome ami onno aktam model theke subquery kore data ene ei model er field ke set kore dicchi.
        salary_subquery = LinkEmpWithAdmin.objects.filter(emp_id=OuterRef('id')).values('salary')[:1]
        datas = datas.annotate(salarys=Subquery(salary_subquery))

        for data in datas:
            data.salary= data.salarys

        serialized_data = AdminSerializers(datas, many=True)
        return Response(serialized_data.data)
    
    def post(self, request):
        post_content = request.data
        # print("Post content =>", post_content)
        serialized_data = AdminSerializers(data=post_content)
        if serialized_data.is_valid():
            # save to database
            serialized_data.save()
            return Response(serialized_data.data, status=status.HTTP_201_CREATED)

        return Response({"Message": serialized_data.errors}, status=status.HTTP_406_NOT_ACCEPTABLE)
    

    def put(self, request):
        Put_content = request.data
        print("PUT content =>", Put_content)

        updatedObj = Admin.objects.get(id= Put_content['id'])
        serialized_data = AdminSerializers(updatedObj,data = Put_content)

        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data)

        return Response({"Message": serialized_data.errors}, status=status.HTTP_406_NOT_ACCEPTABLE)
    
    def patch(self, request):
        patch_content = request.data
        print("PATCH content =>", patch_content)

        updatedObj = Admin.objects.get(id = patch_content['id'])
        serialized_data = AdminSerializers(updatedObj,data = patch_content, partial = True)
        print("Updated object", updatedObj)

        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data)

        return Response({"Message": serialized_data.errors}, status=status.HTTP_406_NOT_ACCEPTABLE)
    
    def delete(self, request):
        request_data = request.data 
        updatedObj = Admin.objects.get(id=request_data['id'])
        updatedObj.delete()
        return Response({"Message": "Entity deleted :)"}, status=status.HTTP_200_OK)


# Django by default curd api deal kore. ModelViewSet er maddhome . This is just for idea it is not the best practice. 


class ModelViewSetExample(viewsets.ModelViewSet):
    serializer_class = AdminSerializers;
    queryset = Admin.objects.all()
