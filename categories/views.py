from django.shortcuts import render
from .models import Category
from django.http import JsonResponse
from django.core import serializers
from rest_framework.decorators import api_view
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT
from categories.serializers import CategorySerializer
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet


class CategoryViewSet(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


# class Categories(APIView):
#     def get(self, request):
#         all_categories = Category.objects.all()
#         serializer = CategorySerializer(all_categories, many=True)
#         return Response(
#             {
#                 "ok": True,
#                 "categories": serializer.data,
#             }
#         )

#     def post(self, request):
#         serializer = CategorySerializer(data=request.data)
#         if serializer.is_valid():
#             new_serializer = serializer.save()
#             return Response(
#                 CategorySerializer(new_serializer).data,
#             )
#         else:
#             return Response(serializer.errors)


# class CategoryDetail(APIView):
#     def get_object(self, pk):
#         try:
#             return Category.objects.get(pk=pk)
#         except Category.DoesNotExist:
#             raise NotFound

#     def get(self, request, pk):
#         category = self.get_object(pk)
#         serializer = CategorySerializer(category)
#         return Response(serializer.data)

#     def put(self, request, pk):
#         category = self.get_object(pk)
#         serializer = CategorySerializer(
#             category,
#             data=request.data,
#             partial=True,
#         )
#         if serializer.is_valid():
#             updated_serializer = serializer.save()
#             return Response(
#                 CategorySerializer(updated_serializer).data,
#             )
#         else:
#             return Response(serializer.errors)

#     def delete(self, reuqest, pk):
#         category = self.get_object(pk)
#         category.delete()
#         return Response(status=HTTP_204_NO_CONTENT)
