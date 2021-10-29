from rest_framework import status, views
from rest_framework.response import Response
from supermercadoApp.models.inventario import Inventario
from supermercadoApp.models.compras import Compra
from supermercadoApp.serializers.CompraSerializer import CompraSerializer


class CompraCreateView(views.APIView):
    queryset = Compra.objects.all()
    serializer_class = CompraSerializer

    def post(self, request, *args, **kwargs):
        serializer = CompraSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        inventario = Inventario.objects.get(id=request.data['inventario_id'])
        inventario.amount -= request.data['amountC']
        inventario.save()
        return Response(status=status.HTTP_201_CREATED)
