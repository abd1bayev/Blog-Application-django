from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User


@api_view(['GET'])
def register(requset):
    data = requset.data

    if data['password'] != data['password_confirm']:
        raise exceptions


@api_view(['GET'])
def users(request):
    users = User.objects.all()
    return Response(users)