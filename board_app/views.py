from rest_framework.viewsets import ModelViewSet
from board_app.models import BoardFlowPost
from board_app.permissions import BoardFlowPostPermission
from board_app.serializers import BoardFlowPostSerializer


class BoardFlowPostViewSet(ModelViewSet):
    """
    정렬을 위해서 queryset -> order_by('-pk')
    permission_classes -> 게시판 비밀번호 검증 로직 적용
    """
    queryset = BoardFlowPost.objects.all().order_by('-pk')
    serializer_class = BoardFlowPostSerializer
    permission_classes = (BoardFlowPostPermission,)

    def perform_create(self, serializer):
        """
        현재 로그인한 유저의 id 를 게시물의 저자로 저장
        """
        serializer.save(author=self.request.user)
        return super().perform_create(serializer)

    def get_serializer_context(self):
        """

        serializer 에 추가 context 제공

        """
        context = super().get_serializer_context()
        context['request'] = self.request
        return context
