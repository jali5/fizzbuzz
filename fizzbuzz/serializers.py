__author__ = 'root'
from models import FizzBuzz
from rest_framework import serializers


class FizzBuzzSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FizzBuzz
        fields = ('fizzbuzz_id', 'useragent', 'creation_date', 'message')
