from rest_framework import serializers
from . models import Todomodel, User


class TodomodelSerializers(serializers.ModelSerializer):
    class Meta:
        model = Todomodel
        fields = ['id','user','title','contents']

class UsermodelSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','UserName','email','password']
class UsernewmodelSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','UserName']

        