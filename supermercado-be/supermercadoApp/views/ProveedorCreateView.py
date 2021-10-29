from rest_framework import status, views
from rest_framework.response import Response
from supermercadoApp.models.proveedores import Proveedor
from supermercadoApp.serializers.ProveedorSerializer import ProveedorSerializer
from rest_framework.permissions import IsAuthenticated


class ProveedorCreateView(views.APIView):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = ProveedorSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)
