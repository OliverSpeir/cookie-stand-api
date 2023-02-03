from rest_framework import generics
from .serializers import CookieStandSerializer
from .models import CookieStand
from .permissions import IsCreatorOrReadOnly


class CookieStandAPIList(generics.ListCreateAPIView):
    queryset = CookieStand.objects.all()
    serializer_class = CookieStandSerializer


class CookieStandAPIDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsCreatorOrReadOnly,)
    queryset = CookieStand.objects.all()
    serializer_class = CookieStandSerializer
