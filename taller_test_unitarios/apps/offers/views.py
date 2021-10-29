from django.http import response
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import Offer
from .serializer import OfferSerializer
from .services import list, create

class OfferView(viewsets.ModelViewSet):
    queryset = list()
    serializer_class = OfferSerializer
    
    def create(self, request, *args, **kwargs):
        response_status = status.HTTP_400_BAD_REQUEST
        response_body = {'success': False}

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            # Create offer
            offer = create(serializer.validated_data)
            response_status = status.HTTP_201_CREATED
            response_body = OfferSerializer(offer).data

        return Response(response_body, status=response_status)