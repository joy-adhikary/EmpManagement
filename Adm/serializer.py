
from rest_framework import serializers
from .models import Admin
from Emp.serializers import EMPSerializers2
from Emp.models import Emp

# Convert queryset ( database info ) to json format or vise-varsa 

class AdminSerializers(serializers.ModelSerializer):
    # to serialize emp data 
    emp = EMPSerializers2()
    # add an extra field into the admin model called emp_userRole_using_serializer
    emp_userRole_using_serializer = serializers.SerializerMethodField()

#  Kon model ke serialize korbo seita ei meta te bole dite hobe 
    class Meta:
        model = Admin
        # show same selected fields
        # fields = ['password', 'username','email']

        # show all fileds 
        fields = '__all__'
        
        # Exclude only name fields . mane amr kase 100 ta model fields ashe, tar majhe ami just name ta show korbo nah.
        # exclude= ['user_type']

        #  jodi kono foreignKey add kora thake tahole eita diye oi foreignkey er obj gular full info pauya jabe ( for example : 
        #  data = { 'name': 'x','age':{'age':'1', 'dob':'12-2-2'}}) ei format a pauya jabe
        depth = 1 



                                                #  validation part 

#  validation function ke 2 vabe likha jai. 
#! First one hocce validate_nameOfTheType. For example ( validate_name, validate_age, validate_gender)
#! Second one hocce just validate likhe oitar majhe if condition diye akta akta kore validate kora. 

# example 1 ( be careful with naming here because it's not only a function name , it's actually an exisiting data )

    # def validate_user_name(self, username):
    #     if username.lower() != 'admin':
    #         raise serializers.ValidationError('User type must be admin')
        
    #     return username
    

# example 2 ( secure way to do it )

    def validate(self,data):
        # userType validation 
        if data['user_type'].lower() != 'admin':
            raise serializers.ValidationError('User type must be admin')
        
        # password validation
        if len(data['password']) < 5 :
            raise serializers.ValidationError('Password must be at least 5 characters')
        
        return data
    
    def get_emp_userRole_using_serializer(self, data):

        # using filter 
        # user_info = Emp.objects.filter(id = data.emp.id)
        # return {'emp_role': user_info[0].role}

        # using get method  
        user_info = Emp.objects.get(id = data.emp.id)

        return {'emp_role': user_info.role}