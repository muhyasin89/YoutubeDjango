from django.db import models
from django.utils.translation import ugettext_lazy as _

from model_utils.models import TimeStampedModel

# Create your models here.
class Answer(TimeStampedModel):
    name =  models.CharField(_('name'), max_length=255, default='Member')
    correct_answer = models.BooleanField(default=False)

    class Meta:
        verbose_name = _('answer')
        verbose_name_plural = _('ansert')