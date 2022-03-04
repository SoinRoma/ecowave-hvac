from rest_framework import serializers

from index.models import FeedbackRequest


class FeedbackRequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = FeedbackRequest
        fields = '__all__'