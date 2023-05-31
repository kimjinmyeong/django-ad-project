from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect

from ..models import Question, Answer, Comment


@login_required(login_url="common:login")
def vote_question(request, question_id):
    """
    pybo 질문 추천 등록
    """
    question = get_object_or_404(Question, pk=question_id)
    validate_already_vote(request, question)
    validate_self_vote(request, question)
    question.voter.add(request.user)
    return redirect("pybo:detail", question_id=question.id)


@login_required(login_url="common:login")
def vote_answer(request, answer_id):
    """
    pybo 답글 추천 등록
    """
    answer = get_object_or_404(Answer, pk=answer_id)
    validate_already_vote(request, answer)
    validate_self_vote(request, answer)
    answer.voter.add(request.user)
    return redirect("pybo:detail", question_id=answer.question.id)


@login_required(login_url="common:login")
def vote_comment(request, comment_id):
    """
    pybo 댓글 추천 등록
    """
    comment = get_object_or_404(Comment, pk=comment_id)
    validate_already_vote(request, comment)
    validate_self_vote(request, comment)
    comment.voter.add(request.user)
    question_id = (
        comment.question.id if comment.question is not None else comment.answer.id
    )
    return redirect("pybo:detail", question_id)


def validate_already_vote(request, model):
    if request.user != model.author and model.voter.filter(id=request.user.id).exists():
        messages.error(request, "이미 추천을 했습니다.")


def validate_self_vote(request, model):
    if request.user == model.author:
        messages.error(request, "본인이 작성한 글은 추천할 수 없습니다")
