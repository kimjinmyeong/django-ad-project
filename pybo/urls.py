from django.urls import path

from .views import (
    page_views,
    question_views,
    answer_views,
    comment_answer_view,
    comment_question_view,
    vote_views,
)

app_name = "pybo"

urlpatterns = [
    # page_views.py
    path("", page_views.index, name="index"),
    path("<int:question_id>/", page_views.detail, name="detail"),
    # question_views.py
    path("questions/create/", question_views.question_create, name="question_create"),
    path(
        "questions/modify/<int:question_id>/",
        question_views.question_modify,
        name="question_modify",
    ),
    path(
        "questions/delete/<int:question_id>/",
        question_views.question_delete,
        name="question_delete",
    ),
    # answer_views.py
    path(
        "answers/create/<int:question_id>/",
        answer_views.answer_create,
        name="answer_create",
    ),
    path(
        "answers/modify/<int:answer_id>/",
        answer_views.answer_modify,
        name="answer_modify",
    ),
    path(
        "answers/delete/<int:answer_id>/",
        answer_views.answer_delete,
        name="answer_delete",
    ),
    # comment_question_view.py
    path(
        "comments/create/questions/<int:question_id>/",
        comment_question_view.comment_create_question,
        name="comment_create_question",
    ),
    path(
        "comments/modify/questions/<int:comment_id>/",
        comment_question_view.comment_modify_question,
        name="comment_modify_question",
    ),
    path(
        "comments/delete/questions/<int:comment_id>/",
        comment_question_view.comment_delete_question,
        name="comment_delete_question",
    ),
    # comment_answer_view.py
    path(
        "comments/create/answers/<int:answer_id>/",
        comment_answer_view.comment_create_answer,
        name="comment_create_answer",
    ),
    path(
        "comments/modify/answers/<int:comment_id>/",
        comment_answer_view.comment_modify_answer,
        name="comment_modify_answer",
    ),
    path(
        "comments/delete/answers/<int:comment_id>/",
        comment_answer_view.comment_delete_answer,
        name="comment_delete_answer",
    ),
    # vote_views.py
    path(
        "vote/questions/<int:question_id>/",
        vote_views.vote_question,
        name="vote_question",
    ),
    path("vote/answers/<int:answer_id>/", vote_views.vote_answer, name="vote_answer"),
    path(
        "vote/comments/<int:comment_id>/",
        vote_views.vote_comment,
        name="vote_comment",
    ),
]
