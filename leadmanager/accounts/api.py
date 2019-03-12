from rest_framework import generics, permissions
from rest_framework.response import Response
from know.models import AuthToken
from .serializers import UserSerializer, RegisterSerializer

# Register API


class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            'user': UserSerializer(user, context=self.get_serializer_context()).data,
            'token': AuthToken.object.create(user)
        })

# Login API

# Get User API
