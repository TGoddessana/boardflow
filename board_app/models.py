from django.contrib.auth.hashers import make_password
from django.db import models
from django.contrib.auth import get_user_model


class TimeStampedModel(models.Model):
    """
    생성된 시간, 수정된 시각을 담는 추상화 모델

    created_at : 객체가 처음 생성되는 시점이 저장됨
    updated_at : 객체가 업데이트 되는 시점이 저장됨
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class BoardFlowPost(TimeStampedModel):
    """
    boardflow 서비스의 게시물 모델

    title : 게시물의 제목
    content : 게시물의 내용
    password : 사용자가 게시물 작성 시 설정하는 비밀번호, 암호화된 상태로 저장됨
    author : 게시물의 저자, Foreign Key 로 django.contrib.auth.models.User 를 참조
    """
    title = models.CharField(max_length=20)
    content = models.CharField(max_length=200)
    password = models.CharField(max_length=200, blank=False, null=False)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return f'<BoardFlowPost Object:{self.title}>'

    def save(self, *args, **kwargs):
        """
        비밀번호 암호화를 위해 save() 메서드를 오버라이딩
        모델 객체에 password 멤버 변수가 있으면,
        password 를 암호화 한 후 저장
        """
        if self.password:
            password = make_password(self.password)
            self.password = password

        return super().save(*args, **kwargs)
