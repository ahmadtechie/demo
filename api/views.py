from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


# Create your views here.
class HomePageView(APIView):
    def get(self, request):
        data = {
            'success': 'Happy coding'
        }
        return Response(data=data, status=status.HTTP_200_OK)