from rest_framework import generics, status
from rest_framework.response import Response
from supermercadoApp.models.proveedores import Proveedor
from supermercadoApp.serializers.ProveedorSerializer import ProveedorSerializer
from rest_framework.permissions import IsAuthenticated


class ProveedorDetailView(generics.RetrieveAPIView):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        pk = kwargs["pk"]
        if Proveedor.objects.filter(id=pk).exists():
            instance = Proveedor.objects.get(pk=pk)
            serializer = ProveedorSerializer(instance)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Proveedor no existe en la base de datos'}, status=status.HTTP_404_NOT_FOUND)
