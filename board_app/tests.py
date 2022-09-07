from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.test import Client
from django.contrib.auth import get_user_model
from board_app.models import BoardFlowPost


class PostGETests(APITestCase):
    """
    게시물 목록에 대한 GET,
    게시물 상세에 대한 GET 테스트
    """

    def setUp(self):
        """
        테스트를 위한 사전 준비
        1. 클라이언트 생성
        2. 유저 두 명 생성
        3. 게시물 300개 생성
        """

        # 요청을 위한 클라이언트 생성
        self.client = Client(enforce_csrf_checks=True)

        # 테스트를 위한 유저 한 명 생성
        self.user_1 = get_user_model()(username="testuser1", password="world")
        self.user_1.save()

        # 테스트를 위한 게시물 999개 생성
        dummy_posts = []
        for i in range(999):
            dummy_posts.append(
                BoardFlowPost(title=f'테스트 게시물입니다.{i + 1}', content=f'테스트 게시물의 내용입니다.{i + 1}', password='12345',
                              author=self.user_1))
        BoardFlowPost.objects.bulk_create(dummy_posts)

    def test_post_list_result(self):
        """
        게시물 목록 조회 테스트
        1. Pagination 은 잘 적용되어 있는가?
        2. 정렬은 최신 게시물 순서 (-pk) 대로 잘 나타나는가?

        더미 게시물은, 아래와 같이 생성될 것이다.
        id -> 1
        title -> 테스트 게시물입니다.1
        content -> 테스트 게시물의 내용입니다.1

        2번째 페이지를 조회했을 때에, 보여주는 게시물의 수는 20개가 되어야 하고,
        보여주는 게시물의 첫 번째 id 는 979가 되어야 한다.
        """

        self.url = reverse('boardflowpost-list')
        response = self.client.get(f'{self.url}?page=2')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 20)
        self.assertEqual(dict(list(response.data['results'])[0])['id'], 979)

    def test_post_detail_result(self):
        """
        게시물 상세 기본 조회 테스트,
        id = 222 인 게시물을 조회한다면,
        아래와 같은 응답이 내용으로 와야 한다. (생성, 수정일자는 제외)
        {
            "id": 222,
            "title": "테스트 게시물입니다.222",
            "content": "테스트 게시물의 내용입니다.222",
            "author_name": "testuser1",
        }

        고로, id=222 인 게시물을 조회한 후
        해당 게시물의 제목이 "테스트 게시물입니다.222" 인지 확인한다.
        """
        self.url = reverse('boardflowpost-list')
        response = self.client.get(f'{self.url}222/')
        self.assertEqual(response.data['title'], "테스트 게시물입니다.222")
