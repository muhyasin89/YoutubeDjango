from django.db import models
from django.utils.translation import ugettext_lazy as _

from model_utils.models import TimeStampedModel

from app.category.models import Category

# Create your models here.
class Quiz(TimeStampedModel):
    name = models.CharField(_('name'), max_length=255, default='Member')
    category = models.ForeignKey(Category, related_name="category", on_delete=models.CASCADE)
    score = models.IntegerField()

    class Meta:
        verbose_name = _('quiz')
        verbose_name_plural = _('quizs')


    def __str__(self):
        return '{}'.format(self.name)
