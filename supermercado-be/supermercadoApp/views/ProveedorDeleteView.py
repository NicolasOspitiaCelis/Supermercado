from rest_framework import generics, status
from rest_framework.response import Response
from supermercadoApp.models.proveedores import Proveedor
from supermercadoApp.serializers.ProveedorSerializer import ProveedorSerializer
from rest_framework.permissions import IsAuthenticated


class ProveedorDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer
    permission_classes = [IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        pk = kwargs["pk"]
        if Proveedor.objects.filter(id=pk).exists():
            instance = Proveedor.objects.get(pk=pk)
            self.perform_destroy(instance)
        else:
            return Response({'message': 'Proveedor no existe en la base de datos'}, status=status.HTTP_404_NOT_FOUND)
        return Response({"message": "Se eliminó el proveedor correctamente"}, status=status.HTTP_200_OK)
