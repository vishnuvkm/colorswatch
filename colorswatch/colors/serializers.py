from rest_framework import serializers


class ColorSpaceSerializer(serializers.Serializer):
    """
    Serializer to return color space and components
    """
    kind = serializers.CharField()
    components = serializers.JSONField()
