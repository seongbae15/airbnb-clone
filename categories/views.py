from django.shortcuts import render
from .models import Category
from django.http import JsonResponse
from django.core import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view()
def categories(request):
    return Response(
        {
            "ok": True,
            "categories": Category.objects.all(),
        }
    )
