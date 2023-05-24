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
    path("question/create/", question_views.question_create, name="question_create"),
    path(
        "question/modify/<int:question_id>/",
        question_views.question_modify,
        name="question_modify",
    ),
    path(
        "question/delete/<int:question_id>/",
        question_views.question_delete,
        name="question_delete",
    ),
    # answer_views.py
    path(
        "answer/create/<int:question_id>/",
        answer_views.answer_create,
        name="answer_create",
    ),
    path(
        "answer/modify/<int:answer_id>/",
        answer_views.answer_modify,
        name="answer_modify",
    ),
    path(
        "answer/delete/<int:answer_id>/",
        answer_views.answer_delete,
        name="answer_delete",
    ),
    # comment_question_view.py
    path(
        "comment/create/question/<int:question_id>/",
        comment_question_view.comment_create_question,
        name="comment_create_question",
    ),
    path(
        "comment/modify/question/<int:comment_id>/",
        comment_question_view.comment_modify_question,
        name="comment_modify_question",
    ),
    path(
        "comment/delete/question/<int:comment_id>/",
        comment_question_view.comment_delete_question,
        name="comment_delete_question",
    ),
    # comment_answer_view.py
    path(
        "comment/create/answer/<int:answer_id>/",
        comment_answer_view.comment_create_answer,
        name="comment_create_answer",
    ),
    path(
        "comment/modify/answer/<int:comment_id>/",
        comment_answer_view.comment_modify_answer,
        name="comment_modify_answer",
    ),
    path(
        "comment/delete/answer/<int:comment_id>/",
        comment_answer_view.comment_delete_answer,
        name="comment_delete_answer",
    ),
    # vote_views.py
    path(
        "vote/question/<int:question_id>/",
        vote_views.vote_question,
        name="vote_question",
    ),
    path(
        "vote/answer/<int:answer_id>/",
         vote_views.vote_answer,
         name="vote_answer"),
    path(
        "vote/question_comment/<int:comment_id>/",
         vote_views.question_vote_comment,
         name="question_vote_comment"),
    path(
        "vote/answer_comment/<int:comment_id>/",
         vote_views.answer_vote_comment,
         name="answer_vote_comment"),
]
