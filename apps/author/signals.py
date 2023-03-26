from datetime import timezone
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from apps.author.models import Author
from apps.change_log.models import ChangeLog




@receiver(post_save,sender=Author)
def log_update(sender,instance,*args,**kwargs):
    ChangeLog.objects.create(
        section='Author',
        option='Update', # this include create
        created = timezone.now()
    )


@receiver(post_delete,sender=Author)
def log_delete(sender,instance,*args,**kwargs):
    ChangeLog.objects.create(
        section='Author',
        option='Delete',
        created = timezone.now()
    )