from wsgiref.validate import validator
from rest_framework import fields, serializers
from .models import Room

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('id', 'code' , 'host' , 'guest_can_pause','votes_to_skip','created_at')
        
class CreateRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('guest_can_pause', 'votes_to_skip')


class UpdateRoomSerilizer(serializers.ModelSerializer):
    code = serializers.CharField(validators=[]) # code will referencing to this field
    # the code field in our models is unique, so if we pass the code to the serializer it will yell that the code is not unique
    # therefore the data is invalid so we should change some of the code up to handle that scenario because all the code that we will pass will already exist in the db

    class Meta :
        model = Room
        fields = ('guest_can_pause', 'votes_to_skip', 'code')


