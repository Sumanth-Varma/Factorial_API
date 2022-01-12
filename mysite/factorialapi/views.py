from rest_framework import viewsets

from .serializers import FactorialNumberSerializer
from .models import FactorialNumber


class FactorialNumberViewSet(viewsets.ModelViewSet):
    queryset = FactorialNumber.objects.all().order_by('number')
    serializer_class = FactorialNumberSerializer