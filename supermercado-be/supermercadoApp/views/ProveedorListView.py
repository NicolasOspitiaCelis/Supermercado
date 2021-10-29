from rest_framework import generics
from supermercadoApp.models.proveedores import Proveedor
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse


class ProveedorListView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        data = list(Proveedor.objects.values())
        return JsonResponse(data, safe=False)
