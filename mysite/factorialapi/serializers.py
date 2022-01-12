from rest_framework import serializers

from .models import FactorialNumber

class FactorialNumberSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FactorialNumber
        fields = ('number','factorial',)