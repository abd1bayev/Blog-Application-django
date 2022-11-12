from rest_framework import serializers
from .models import User

class UserSerializers(serializers.ModelSerializer):
    class Metta:
        model = User
        fields = ['id', 'first_name','last_name','email', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }