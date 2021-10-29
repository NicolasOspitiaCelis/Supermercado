from rest_framework import status, views
from rest_framework.response import Response
from supermercadoApp.models.productos import Producto
from supermercadoApp.serializers.ProductoSerializer import ProductoSerializer
from rest_framework.permissions import IsAuthenticated


class ProductoCreateView(views.APIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = ProductoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)
