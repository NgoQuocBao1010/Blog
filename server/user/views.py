from rest_framework import generics
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status


from user.models import User
from user.api.serializers import (
    UserRegisterSerializer,
    UserSerializer,
    AuthCustomTokenSerializer,
)


class ListRegisterView(generics.ListCreateAPIView):
    def get_queryset(self):
        if self.request.method == "POST":
            return User.objects.all()
        return User.objects.exclude(pk=self.request.user.pk).order_by("-created_at")
    
    def get_permissions(self):
        if self.request.method == "POST":
            return [AllowAny()]
        
        return [IsAuthenticated()]
    
    def get_serializer_class(self):
        if self.request.method == "POST":
            return UserRegisterSerializer

        # If "GET"
        return UserSerializer


class LoginView(ObtainAuthToken):
    serializer_class = AuthCustomTokenSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        token, created = Token.objects.get_or_create(user=user)
        return Response({"token": token.key, "user_id": user.pk, "email": user.email})
    

class UserDelteView(generics.DestroyAPIView):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]
    lookup_field = "email"

    def delete(self, request, *args, **kwargs):
        # Get the model instance
        instance: User = self.get_object()

        

        if (instance.email == request.user.email):
            return Response(
                {"detail": "Cannot delete your own account"}, status=status.HTTP_400_BAD_REQUEST
            )
        
        # Simply delete - no need to instantiate the serializer
        self.perform_destroy(instance)
        

        return Response(
            {"message": "Deleted Successfully"}, status=status.HTTP_204_NO_CONTENT
        )
