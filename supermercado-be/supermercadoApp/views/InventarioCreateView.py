from rest_framework import status, views
from rest_framework.response import Response
from supermercadoApp.models.inventario import Inventario
from supermercadoApp.serializers.InventarioSerializer import InventarioSerializer
from rest_framework.permissions import IsAuthenticated


class InventarioCreateView(views.APIView):
    queryset = Inventario.objects.all()
    serializer_class = InventarioSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = InventarioSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)
