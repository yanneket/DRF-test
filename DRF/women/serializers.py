from ast import Delete
from rest_framework import serializers
from .models import Women
from rest_framework.response import Response


class WomenSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Women
        fields = "__all__"
