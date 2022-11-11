from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User

@api_view(['GET'])
def users(request):
    users = User.objects.all()
    return Response(users)