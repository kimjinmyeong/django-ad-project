from django.test import TestCase
from django.contrib.auth.models import User
from django.utils import timezone

from .models import Question


class QuestionCreateTests(TestCase):
    def setUp(self) -> None:
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
    def setUp(self) -> None:
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
    def setUp(self) -> None:
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
    def setUp(self) -> None:
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
