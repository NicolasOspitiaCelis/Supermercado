from rest_framework import status, views
from rest_framework.response import Response
from supermercadoApp.models.user import User
from supermercadoApp.serializers.UserSerializer import UserSerializer
from rest_framework.permissions import IsAuthenticated


class UserCreateView(views.APIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)
