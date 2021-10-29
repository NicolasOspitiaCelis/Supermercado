from rest_framework import generics, status
from rest_framework.response import Response
from supermercadoApp.models.inventario import Inventario
from supermercadoApp.serializers.InventarioSerializer import InventarioSerializer
from rest_framework.permissions import IsAuthenticated


class InventarioDetailView(generics.RetrieveAPIView):
    queryset = Inventario.objects.all()
    serializer_class = InventarioSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        pk = kwargs["pk"]
        if Inventario.objects.filter(id=pk).exists():
            instance = Inventario.objects.get(pk=pk)
            serializer = InventarioSerializer(instance)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Proveedor no existe en la base de datos'}, status=status.HTTP_404_NOT_FOUND)
