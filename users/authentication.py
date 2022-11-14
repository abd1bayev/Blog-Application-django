import jwt
import datetime
from django.conf import settings

def generate_access_token(user):
    payload = {
        'user_id':user.id,
        'ext': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
        'iat': datetime.datetime.utcnow()
    }

    return jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256').decode('utf-8')
