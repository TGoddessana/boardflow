from django.contrib.auth.hashers import check_password
from rest_framework import permissions


class BoardFlowPostPermission(permissions.BasePermission):
    """
    게시물 삭제, 수정 시 비밀번호 검증, 비밀번호가 일치하지 않을 시 403 상태 코드와 에러 메시지 반환
    """

    def has_object_permission(self, request, view, obj):
        """
        GET / OPTION / HEAD 에 대해서는 True 반환
        PUT / DELETE / POST 에 대해서는 비밀번호 검증 후, True or False 반환

        Args:
            request: <class 'rest_framework.request.Request'>
            view: <class 'board_app.views.BoardFlowPostViewSet'>
            obj: <class 'board_app.models.BoardFlowPost'>

        Returns:

        """
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return check_password(request.data.get('password'), obj.password)
