
from rest_framework import serializers
from .models import Admin

# Convert queryset ( database info ) to json format or vise-varsa 

class AdminSerializers(serializers.ModelSerializer):

#  Kon model ke serialize korbo seita ei meta te bole dite hobe 
    class Meta:
        model = Admin
        # show same selected fields
        fields = ['password', 'username','email']

        # show all fileds 
        fields = '__all__'
        
        # Exclude only name fields . mane amr kase 100 ta model fields ashe, tar majhe ami just name ta show korbo nah.
        exclude= ['user_type']
