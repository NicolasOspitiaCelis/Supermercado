from rest_framework import generics
from supermercadoApp.models.user import User
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse


class UserListView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        data = list(User.objects.values())
        return JsonResponse(data, safe=False)
