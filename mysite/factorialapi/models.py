from django.db import models
import math

class FactorialNumber(models.Model):
    number = models.IntegerField()

    @property
    def factorial(self):
        return math.factorial(self.number)

    def __all__(self):
        return self.number