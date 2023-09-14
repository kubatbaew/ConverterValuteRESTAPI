from rest_framework import serializers

from apps.converter.models import Converter


class ConverterSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Converter
        fields = (
            "id",
            "from_currency",
            "to_currency",
            "value",
            "get_value_currency",
        )
