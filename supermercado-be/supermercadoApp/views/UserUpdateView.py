from rest_framework import status, generics
from rest_framework.response import Response
from supermercadoApp.serializers.UserSerializer import UserSerializer
from django.forms.models import model_to_dict
from supermercadoApp.models.user import User
from rest_framework.permissions import IsAuthenticated


class UserUpdateView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def put(self, request, *args, **kwargs):
        pk = kwargs["pk"]
        instance = User.objects.get(pk=pk)
        serializer = UserSerializer(instance=instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.update(instance, validated_data=request.data)
        return Response(model_to_dict(instance), status=status.HTTP_201_CREATED)
