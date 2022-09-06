from rest_framework.viewsets import ModelViewSet
from board_app.models import BoardFlowPost
from board_app.serializers import BoardFlowPostSerializer


class BoardFlowPostViewSet(ModelViewSet):
    queryset = BoardFlowPost.objects.all()
    serializer_class = BoardFlowPostSerializer

    def perform_create(self, serializer):
        """
        현재 로그인한 유저의 id 를 게시물의 저자로 저장
        """
        serializer.save(author=self.request.user)
        return super().perform_create(serializer)
