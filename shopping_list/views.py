from rest_framework import generics
from shopping_list.api.permissions import (
    AllShoppingItemsShoppingListMembersOnly,
    ShoppingItemShoppingListMembersOnly,
    ShoppingListMembersOnly,
)
from shopping_list.api.serializers import ShoppingListSerializer, ShoppingItemSerializer
from shopping_list.models import ShoppingList, ShoppingItem

class ListAddShoppingList(generics.ListCreateAPIView):
    queryset = ShoppingList.objects.all()
    serializer_class = ShoppingListSerializer
    
    def perform_create(self, serializer):
        return serializer.save(members=[self.request.user])
    
    def get_queryset(self):
        return ShoppingList.objects.filter(members=self.request.user)

class ShoppingListDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ShoppingList.objects.all()
    serializer_class = ShoppingListSerializer
    
    permission_classes = [ShoppingListMembersOnly]
    
# class AddShoppingItem(generics.CreateAPIView):
#     queryset = ShoppingItem.objects.all()
#     serializer_class = ShoppingItemSerializer
    
#     permission_classes = [AllShoppingItemsShoppingListMembersOnly]
    
class ShoppingItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ShoppingItem.objects.all()
    serializer_class = ShoppingItemSerializer
    lookup_url_kwarg = "item_pk"
    
    permission_classes = [ShoppingItemShoppingListMembersOnly]
    
class ListAddShoppingItem(generics.ListCreateAPIView):
    serializer_class = ShoppingItemSerializer
    permission_classes = [AllShoppingItemsShoppingListMembersOnly]
    
    def get_queryset(self):
        shopping_list = self.kwargs["pk"]
        return ShoppingItem.objects.filter(shopping_list=shopping_list)