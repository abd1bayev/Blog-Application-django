from rest_framework import exceptions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializers
from .models import User


@api_view(['POST'])
def register(requset):
    data = requset.data

    if data['password'] != data['password_confirm']:
        raise exceptions.APIException('Passwords do not match!')

    serializer = UserSerializers(data=data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)


@api_view(['GET'])
def users(request):
    serializer = UserSerializers(User.objects.all(), many=True)
    return Response(serializer)