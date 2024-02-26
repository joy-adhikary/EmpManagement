
from rest_framework import serializers
from .models import Emp

# Convert queryset ( database info ) to json format or vise-varsa 

class EMPSerializers(serializers.ModelSerializer):

#  Kon model ke serialize korbo seita ei meta te bole dite hobe 
    class Meta:
        model = Emp
        # show some selected fields
        # fields = ['password', 'username','email']

        # show all fileds 
        fields = '__all__'
        
        # Exclude only name fields . mane amr kase 100 ta model fields ashe, tar majhe ami just name ta show korbo nah.
        # exclude= ['user_type']
