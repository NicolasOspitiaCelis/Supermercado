from rest_framework import status, generics
from rest_framework.response import Response
from django.forms.models import model_to_dict
from supermercadoApp.models.inventario import Inventario
from supermercadoApp.serializers.InventarioSerializer import InventarioSerializer
from rest_framework.permissions import IsAuthenticated


class InventarioUpdateView(generics.UpdateAPIView):
    queryset = Inventario.objects.all()
    serializer_class = InventarioSerializer
    permission_classes = [IsAuthenticated]

    def put(self, request, *args, **kwargs):
        pk = kwargs["pk"]
        instance = Inventario.objects.get(pk=pk)
        serializer = InventarioSerializer(instance=instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.update(instance, validated_data=request.data)
        return Response(model_to_dict(instance), status=status.HTTP_201_CREATED)
