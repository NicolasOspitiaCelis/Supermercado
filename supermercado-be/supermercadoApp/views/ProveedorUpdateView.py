from rest_framework import status, generics
from rest_framework.response import Response
from django.forms.models import model_to_dict
from supermercadoApp.models.proveedores import Proveedor
from supermercadoApp.serializers.ProveedorSerializer import ProveedorSerializer
from rest_framework.permissions import IsAuthenticated


class ProveedorUpdateView(generics.UpdateAPIView):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer
    permission_classes = [IsAuthenticated]

    def put(self, request, *args, **kwargs):
        pk = kwargs["pk"]
        instance = Proveedor.objects.get(pk=pk)
        serializer = ProveedorSerializer(instance=instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.update(instance, validated_data=request.data)
        return Response(model_to_dict(instance), status=status.HTTP_201_CREATED)
