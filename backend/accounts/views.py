from rest_framework.views import APIView
from rest_framework.response import Response

from .models import User
from .services import PasswordService
from .jwt_service import JWTService
from .serializers import RegisterSerializer


# ---------------- REGISTER ----------------
class RegisterView(APIView):

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=400)

        email = serializer.validated_data["email"]
        password = serializer.validated_data["password"]
        name = serializer.validated_data["name"]
        role = serializer.validated_data["role"]

        # check if user exists
        if User.objects(email=email).first():
            return Response({"error": "User already exists"}, status=400)

        hashed_password = PasswordService.hash_password(password)

        user = User.objects.create(
            email=email,
            password=hashed_password,
            name=name,
            role=role
        )

        return Response({
            "message": "User registered successfully",
            "user_id": str(user.id)
        })



# ---------------- LOGIN ----------------
class LoginView(APIView):

    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")

        user = User.objects(email=email).first()

        if not user:
            return Response({"error": "Invalid user"}, status=400)

        if not PasswordService.verify_password(password, user.password):
            return Response({"error": "Wrong password"}, status=400)

        return Response(JWTService.create_tokens(user))