from django.conf import settings
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.backends import TokenBackend
from supermercadoApp.models.user import User
from supermercadoApp.serializers.UserSerializer import UserSerializer
from rest_framework.permissions import IsAuthenticated


class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        token = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tokenBackend.decode(token, verify=False)
        if User.objects.filter(id=valid_data['user_id']).exists():
            return super().get(request, *args, **kwargs)
        stringResponse = {'detail': 'El usuario no existe'}
        return Response(stringResponse, status=status.HTTP_404_NOT_FOUND)
