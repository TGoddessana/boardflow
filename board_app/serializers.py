from rest_framework import serializers
from board_app.models import BoardFlowPost
from django.contrib.auth.hashers import check_password


class BoardFlowPostSerializer(serializers.ModelSerializer):
    """
    BoardFlowPost 게시물을 다루기 위한 serializer
    password 만 write_only=True, 입력만 가능하도록
    """
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

    # def update(self, instance, validated_data):
        """
        serialzer 로부터 검증된 데이터를 받아 게시물을 수정
        update 시, 비밀번호가 일치하지 않는다면 에러

        Args:
            instance: BoardFlowPost 의 객체
            validated_data: serializer 에서 검증된 데이터

        """
        # print(check_password(validated_data.get('password'), instance.password))
        # if check_password(validated_data.get('password'), instance.password):
        #     return super().update(instance, validated_data)
