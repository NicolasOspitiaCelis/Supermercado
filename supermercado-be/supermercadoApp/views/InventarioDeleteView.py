from rest_framework import generics, status
from rest_framework.response import Response
from supermercadoApp.models.inventario import Inventario
from supermercadoApp.serializers.InventarioSerializer import InventarioSerializer
from rest_framework.permissions import IsAuthenticated


class InventarioDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Inventario.objects.all()
    serializer_class = InventarioSerializer
    permission_classes = [IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        pk = kwargs["pk"]
        if Inventario.objects.filter(id=pk).exists():
            instance = Inventario.objects.get(pk=pk)
            self.perform_destroy(instance)
        else:
            return Response({'message': 'Proveedor no existe en la base de datos'}, status=status.HTTP_404_NOT_FOUND)
        return Response({"message": "Se eliminó el proveedor correctamente"}, status=status.HTTP_200_OK)
