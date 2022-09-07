from rest_framework import serializers
from board_app.models import BoardFlowPost


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

    def validate_password(self, value):
        """
        클라이언트로부터 들어온 password 데이터가 아래 조건에 맞는지 검증한다.
        1. 비밀번호는 6자 이상인가?
        2. 숫자가 무조건 한 개 이상 포함되어 있는가?

        Args:
            value: password

        Returns: 비밀번호 검증이 성공한다면 비밀번호 값을, 아니라면 ValidationError 를 발생시킨다.

        """

        if len(value) < 6:
            raise serializers.ValidationError("비밀번호는 최소 6자 이상이어야 합니다.")
        elif not any(char.isdigit() for char in value):
            raise serializers.ValidationError('비밀번호에는 최소 한 개의 숫자가 포함되어야 합니다.')
        return value