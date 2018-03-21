from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """Test Api view"""

    def get(self, request, format=None):
        """Returns a list of APIView features."""
        
        an_apiview = [
            "Uses HTTP methods as functions (GET, POST, PUT, PATCH, DELETE)",
            "It is similar to traditional Django view",
            "Gives you the most control over your logic",
            "Is mapped manually to URLs"
        ]
        return Response({"message": "Hello", "an_apiview": an_apiview})