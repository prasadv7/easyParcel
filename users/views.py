from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .serializers import RegisterSerializer, UserSerializer
from .models import CustomUser
from rest_framework.permissions import IsAuthenticated

class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(UserSerializer(user).data, status=201)
        return Response(serializer.errors, status=400)


class ProtectedDataView(APIView):
    permission_classes = [IsAuthenticated] 

    def get(self, request):
        return Response({
            "message": "This is protected data!",
            "user": {
                "username": request.user.username,
                "email": request.user.email,
                "is_authenticated": request.user.is_authenticated,
            },
        })