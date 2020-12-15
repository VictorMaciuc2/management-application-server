from functools import wraps

import jwt
from flask import request, Response, jsonify


def auth_required(func):
    """
    View decorator - require valid access token
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            jwt.decode(request.headers.get('Authorization'), 'super-secret-key', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            return Response('Signature expired', 401)
        except jwt.InvalidTokenError:
            return Response('Invalid token.', 401)
        except:
            Response('Unauthorized', 401)

        return func(*args, **kwargs)
    return wrapper