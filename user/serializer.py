from rest_framework import serializers
from .models import User



class UserSerializer(serializers.ModelSerializer):
    confirm = serializers.CharField(max_length=55)

    def validate(self,data):
        password = data.get("password")
        confirm = data.get("confirm")
        if password != confirm:
            raise serializers.ValidationError("Password confirmatioin Error!")
        return data

    class Meta:
        model  = User
        fields = ['username','password','first_name','last_name','email','confirm']

    