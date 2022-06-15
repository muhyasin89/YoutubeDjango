from django.db import models
from django.utils.translation import ugettext_lazy as _

from model_utils.models import TimeStampedModel
# Create your models here.
class Category(TimeStampedModel):
    name =  models.CharField(_('name'), max_length=255, default='Member')

    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _('categories')