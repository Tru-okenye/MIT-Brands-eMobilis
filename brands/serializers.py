from .models import Brands

from rest_framework import serializers

class BrandSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Brands
        fields = '__all__'