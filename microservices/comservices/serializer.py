from rest_framework import serializers
from .models import CompanyList

class CompanyListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyList
        fields = '__all__'
