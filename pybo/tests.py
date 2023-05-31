from django.test import TestCase
from django.contrib.auth.models import User
from django.utils import timezone

from .models import Question, Comment, Answer


class QuestionCreateTests(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        User.objects.create_user(username="testuser", password="testpassword")

    def test_create_no_login(self):
        response = self.client.get("/pybo/questions/create/")

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, "/common/login/?next=/pybo/questions/create/")

    def test_create_login(self):
        self.client.login(username="testuser", password="testpassword")
        response = self.client.get("/pybo/questions/create/")

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "pybo/question_form.html")


class QuestionModifyTests(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        User.objects.create_user(username="testuser", password="testpassword")
        user = User.objects.get(username="testuser")
        Question.objects.create(
            subject="test question",
            content="test content",
            author=user,
            create_date=timezone.now(),
            modify_date=timezone.now(),
        )

    def test_modify_no_author(self):
        User.objects.create_user(username="noauthoruser", password="testpassword")
        question = Question.objects.get(subject="test question")

        self.client.login(username="noauthoruser", password="testpassword")
        response = self.client.get(f"/pybo/questions/modify/{question.id}/")

        self.assertEqual(response.status_code, 302)

    def test_modify_author(self):
        self.client.login(username="testuser", password="testpassword")
        question = Question.objects.get(subject="test question")
        response = self.client.get(f"/pybo/questions/modify/{question.id}/")

        self.assertEqual(response.status_code, 200)


class QuestionDeleteTests(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        User.objects.create_user(username="testuser", password="testpassword")
        user = User.objects.get(username="testuser")
        Question.objects.create(
            subject="test question",
            content="test content",
            author=user,
            create_date=timezone.now(),
            modify_date=timezone.now(),
        )

    def test_delete_no_author(self):
        User.objects.create_user(username="noauthoruser", password="testpassword")
        question = Question.objects.get(subject="test question")

        self.client.login(username="noauthoruser", password="testpassword")
        response = self.client.get(f"/pybo/questions/delete/{question.id}/")

        self.assertEqual(response.status_code, 302)
        self.assertTrue(Question.objects.filter(id=question.id).exists())

    def test_delete_author(self):
        self.client.login(username="testuser", password="testpassword")
        question = Question.objects.get(subject="test question")
        response = self.client.get(f"/pybo/questions/delete/{question.id}/")

        # Redirect in Django giving 302 response
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Question.objects.filter(id=question.id).exists())


class VoteQuestionTests(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        User.objects.create_user(username="testuser", password="testpassword")
        user = User.objects.get(username="testuser")
        Question.objects.create(
            subject="test question",
            content="test content",
            author=user,
            create_date=timezone.now(),
            modify_date=timezone.now(),
        )

    def test_self_vote_question(self):
        self.client.login(username="testuser", password="testpassword")
        question = Question.objects.get(subject="test question")
        response = self.client.get(f"/pybo/vote/questions/{question.id}/")

        self.assertEqual(response.status_code, 302)
        self.assertEqual(question.voter.count(), 0)

    def test_vote_question(self):
        User.objects.create_user(username="noauthoruser", password="testpassword")
        self.client.login(username="noauthoruser", password="testpassword")
        question = Question.objects.get(subject="test question")
        response = self.client.get(f"/pybo/vote/questions/{question.id}/")

        self.assertEqual(response.status_code, 302)
        self.assertEqual(question.voter.count(), 1)

    def test_vote_twice_question(self):
        User.objects.create_user(username="noauthoruser", password="testpassword")
        self.client.login(username="noauthoruser", password="testpassword")
        question = Question.objects.get(subject="test question")

        self.client.get(f"/pybo/vote/questions/{question.id}/")
        response = self.client.get(f"/pybo/vote/questions/{question.id}/")

        self.assertEqual(response.status_code, 302)
        self.assertEqual(question.voter.count(), 1)


class CountModificationTests(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        User.objects.create_user(username="testuser", password="testpassword")
        user = User.objects.get(username="testuser")
        Question.objects.create(
            subject="test question",
            content="test content",
            author=user,
            create_date=timezone.now(),
            modify_date=timezone.now(),
        )
        question = Question.objects.get(subject="test question")
        Comment.objects.create(
            author=user,
            content="test comment",
            create_date=timezone.now(),
            question=question,
        )
        Answer.objects.create(
            author=user,
            question=question,
            content="test answer",
            create_date=timezone.now(),
        )

    def test_count_modification_question(self):
        self.client.login(username="testuser", password="testpassword")
        question = Question.objects.get(subject="test question")

        self.client.post(
            f"/pybo/questions/modify/{question.id}/",
            {
                "subject": "제목1",
                "content": "내용1",
            },
        )
        self.client.post(
            f"/pybo/questions/modify/{question.id}/",
            {
                "subject": "제목2",
                "content": "내용2",
            },
        )
        response = self.client.post(
            f"/pybo/questions/modify/{question.id}/",
            {
                "subject": "제목3",
                "content": "내용3",
            },
        )
        question.refresh_from_db()

        self.assertEqual(response.status_code, 302)
        self.assertEqual(question.modify_counter, 3)

    def test_count_modification_comment(self):
        self.client.login(username="testuser", password="testpassword")
        comment = Comment.objects.get(content="test comment")

        self.client.post(
            f"/pybo/comments/modify/questions/{comment.id}/",
            {
                "content": "댓글 내용1",
            },
        )
        self.client.post(
            f"/pybo/comments/modify/questions/{comment.id}/",
            {
                "content": "댓글 내용2",
            },
        )
        response = self.client.post(
            f"/pybo/comments/modify/questions/{comment.id}/",
            {
                "content": "댓글 내용3",
            },
        )
        comment.refresh_from_db()

        self.assertEqual(response.status_code, 302)
        self.assertEqual(comment.modify_counter, 3)

    def test_count_modification_answer(self):
        self.client.login(username="testuser", password="testpassword")
        answer = Answer.objects.get(content="test answer")

        self.client.post(
            f"/pybo/answers/modify/{answer.id}/",
            {
                "content": "답 내용1",
            },
        )
        self.client.post(
            f"/pybo/answers/modify/{answer.id}/",
            {
                "content": "답변 내용2",
            },
        )
        response = self.client.post(
            f"/pybo/answers/modify/{answer.id}/",
            {
                "content": "답변 내용3",
            },
        )
        answer.refresh_from_db()

        self.assertEqual(response.status_code, 302)
        self.assertEqual(answer.modify_counter, 3)
