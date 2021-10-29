from rest_framework import status, generics
from rest_framework.response import Response
from django.forms.models import model_to_dict
from supermercadoApp.models.productos import Producto
from supermercadoApp.serializers.ProductoSerializer import ProductoSerializer
from rest_framework.permissions import IsAuthenticated


class ProductoUpdateView(generics.UpdateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    permission_classes = [IsAuthenticated]

    def put(self, request, *args, **kwargs):
        pk = kwargs["pk"]
        instance = Producto.objects.get(pk=pk)
        serializer = ProductoSerializer(instance=instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.update(instance, validated_data=request.data)
        return Response(model_to_dict(instance), status=status.HTTP_201_CREATED)
