from rest_framework.generics import CreateAPIView

from index.serializers import FeedbackRequestSerializer


class CreateFeedbackRequestView(CreateAPIView):
    serializer_class = FeedbackRequestSerializer