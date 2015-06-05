from fizzbuzz.models import FizzBuzz
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.response import Response
from fizzbuzz.serializers import FizzBuzzSerializer


class FizzBuzzViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = FizzBuzz.objects.all()
    serializer_class = FizzBuzzSerializer

    def list(self, request):
        queryset = FizzBuzz.objects.all()
        serializer = FizzBuzzSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = FizzBuzz.objects.all()
        fizzbuzz = get_object_or_404(queryset, pk=pk)
        serializer = FizzBuzzSerializer(fizzbuzz)
        return Response(serializer.data)

    def create(self, request):
        fizzbuzz = FizzBuzz.objects.create(message=request.data['message'], useragent=request.META['HTTP_USER_AGENT'])
        serializer = FizzBuzzSerializer(fizzbuzz)
        return Response(serializer.data, status=status.HTTP_201_CREATED)