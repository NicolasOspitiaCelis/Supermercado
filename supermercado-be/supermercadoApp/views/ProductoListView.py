from rest_framework import generics
from supermercadoApp.models.productos import Producto
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse


class ProductoListView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        data = list(Producto.objects.values())
        return JsonResponse(data, safe=False)
