from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import MenuItem
from .serializers import MenuItemSerializer

# Create your views here.
class MenuItemView(ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer


class SingleMenuItemView(RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

