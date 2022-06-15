from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

from model_utils.models import TimeStampedModel

from app.user_detail import GENDER

# Create your models here.

class userDetail(TimeStampedModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    gender = models.CharField(
        _('gender'), max_length=30, choices=GENDER, blank=True, default=''
    )

    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _('categories')