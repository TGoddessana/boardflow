from django.contrib import admin
from board_app.models import BoardFlowPost


@admin.register(BoardFlowPost)
class BoardFlowPost(admin.ModelAdmin):
    """
    관리자 페이지에 BoardFlowPost 모델 등록
    """
    pass
