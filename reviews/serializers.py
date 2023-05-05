from rest_framework import serializers
from .models import *



class ReviewListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['content']

