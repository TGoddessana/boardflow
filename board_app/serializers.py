from rest_framework import serializers
from board_app.models import BoardFlowPost


class BoardFlowPostSerializer(serializers.ModelSerializer):
    author_name = serializers.SlugRelatedField(read_only=True, slug_field='username', source='author')
    password = serializers.CharField(write_only=True)

    class Meta:
        model = BoardFlowPost
        fields = ["id",
                  "created_at",
                  "updated_at",
                  "title",
                  "content",
                  "password",
                  "author_name"]
