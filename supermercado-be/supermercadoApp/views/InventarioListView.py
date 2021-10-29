from rest_framework import generics
from supermercadoApp.models.inventario import Inventario
from django.http import JsonResponse


class InventarioListView(generics.RetrieveAPIView):

    def get(self, request):
        data = list(Inventario.objects.values())
        return JsonResponse(data, safe=False)
