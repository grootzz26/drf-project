from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets
from .models import categories, product, Added_by
from .serializers import AddedBySerializer, CategorySerializer, ProductSerializer
# Create your views here.

class categoriesAV(viewsets.ModelViewSet):

    queryset = categories.objects.all()
    serializer_class = CategorySerializer

# @api_view(['GET', 'POST'])
# def productAV(request):
#     if request.method == 'GET':
#         data = product.objects.all()
#         serializer = ProductSerializer(data, many=True)
#         return Response(serializer.data)
#
#     if request.method == 'POST':
#         serializer = ProductSerializer(data = request.data)
#         data_set = {}
#         if serializer.is_valid():
#             data = serializer.save()
#
#             data_set['name'] = data.name
#             data_set['type'] = data.type
#             data_set['price'] = data.price
#             data_set['tax'] = data.tax
#             data_set['total_price'] = data.total_price
#             #
#             # Added_by.objects.create(user=request.user, items=data.id)
#             # data['user'] = request.user
#             # data['items'] = data.id
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
class productAV(viewsets.ModelViewSet):

    queryset = product.objects.all()
    serializer_class = ProductSerializer

    # def perform_create(self, serializer):
    #     data = serializer.create()
    #     print(data)
    #     # Added_by.objects.create(user = self.request.user)

class AddedByAV(viewsets.ModelViewSet):

    queryset = Added_by.objects.all()
    serializer_class = AddedBySerializer


