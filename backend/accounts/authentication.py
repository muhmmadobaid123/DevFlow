from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import AccessToken
from accounts.models import User

class MongoJWTAuthentication(BaseAuthentication):
    def authenticate(self, request):
        auth_header = request.headers.get("Authorization")
        if not auth_header:
            return None
        
        parts = auth_header.split()
        if len(parts) != 2 or parts[0].lower() != "bearer":
            return None
        
        token_str = parts[1]
        try:
            token = AccessToken(token_str)
            user_id = token.get("user_id")
            if not user_id:
                raise AuthenticationFailed("Token has no user_id")
            
            user = User.objects(id=user_id).first()
            if not user:
                raise AuthenticationFailed("User not found")
            
            # DRF requires is_authenticated to be True on the authenticated user object.
            # We dynamically set/ensure this attribute.
            user.is_authenticated = True
            
            return (user, token)
        except Exception as e:
            raise AuthenticationFailed(str(e))
