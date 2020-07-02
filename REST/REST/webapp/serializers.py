from rest_framework import serializers
from .models import emp


class empSerializer(serializers.ModelSerializer):

    class Meta:
        model=emp
        fields = '__all__'
       #fields=('firstname','lastname')