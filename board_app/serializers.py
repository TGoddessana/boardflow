from rest_framework import serializers
from board_app.models import BoardFlowPost


class BoardFlowPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BoardFlowPost
        fields = "__all__"
