from rest_framework import serializers
from .models import User

class UserSerializers(serializers.ModelSerializer):
    class Metta:
        model = User
        fields = '__all__'