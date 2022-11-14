from rest_framework import serializers
from .models import User

class UserSerializers(serializers.ModelSerializer):
    class Metta:
        model = User
        fields = ['id', 'first_name','last_name','email', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

        def create(self, validated_data):
            password = validated_data.pop('password', None)
            instanse = self.Meta.model(**validated_data)
            if password is not None:
                instanse.set_password(password)
            instanse.save()
            return instanse