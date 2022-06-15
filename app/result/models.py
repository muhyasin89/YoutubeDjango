from pyexpat import model
from unicodedata import category
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.utils.translation import ugettext_lazy as _

from app.category.models import Category

from model_utils.models import TimeStampedModel
# Create your models here.
class Result(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, related_name="category", on_delete=models.CASCADE)
    total_score = models.IntegerField()

    class Meta:
        verbose_name = _('result')
        verbose_name_plural = _('result')
