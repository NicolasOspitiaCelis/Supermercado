from rest_framework import generics, status
from rest_framework.response import Response
from supermercadoApp.models.productos import Producto
from supermercadoApp.serializers.ProductoSerializer import ProductoSerializer
from rest_framework.permissions import IsAuthenticated


class ProductoDetailView(generics.RetrieveAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        pk = kwargs["pk"]
        if Producto.objects.filter(id=pk).exists():
            instance = Producto.objects.get(pk=pk)
            serializer = ProductoSerializer(instance)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Proveedor no existe en la base de datos'}, status=status.HTTP_404_NOT_FOUND)
