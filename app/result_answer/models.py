from django.db import models
from django.utils.translation import ugettext_lazy as _
from app.answer.models import Answer

from model_utils.models import TimeStampedModel

from app.result.models import Result
from app.quiz.models import Quiz
from app.answer.models import Answer
# Create your models here.
class resultAnswer(TimeStampedModel):
    result = models.ForeignKey(Result, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, related_name="quiz", on_delete=models.CASCADE)
    your_answer = models.ForeignKey(Answer, related_name="answer", on_delete=models.CASCADE)
    score = models.IntegerField()

    class Meta:
        verbose_name = _('result_answer')
        verbose_name_plural = _('result_answers')