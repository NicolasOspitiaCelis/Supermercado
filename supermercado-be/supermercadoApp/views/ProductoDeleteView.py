from rest_framework import generics, status
from rest_framework.response import Response
from supermercadoApp.models.productos import Producto
from supermercadoApp.serializers.ProductoSerializer import ProductoSerializer
from rest_framework.permissions import IsAuthenticated


class ProductoDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    permission_classes = [IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        pk = kwargs["pk"]
        if Producto.objects.filter(id=pk).exists():
            instance = Producto.objects.get(pk=pk)
            self.perform_destroy(instance)
        else:
            return Response({'message': 'Proveedor no existe en la base de datos'}, status=status.HTTP_404_NOT_FOUND)
        return Response({"message": "Se eliminó el proveedor correctamente"}, status=status.HTTP_200_OK)
