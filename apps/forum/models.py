from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from django.contrib.auth.models import User

from . import managers

from django.dispatch import receiver
from django.db.models.signals import post_save
 
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_profile_for_new_user(sender, created, instance, **kwargs):
    if created:
        profile = Profile(user=instance)
        profile.save()

class Profile(models.Model):
    # Relations
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        related_name="profile",
        verbose_name=_("user"),
        on_delete=models.DO_NOTHING,
        )
    # Attributes - Mandatory
    # Attributes - Optional
    # Object Manager
    objects = managers.ProfileManager()
 
    # Custom Properties
    @property
    def username(self):
        return self.user.username
 
    # Methods
 
    # Meta and String
    class Meta:
        verbose_name = _("Profile")
        verbose_name_plural = _("Profiles")
        ordering = ("user",)
 
    def __str__(self):
        return self.user.username

class Category(models.Model):
    cat_name = models.CharField(max_length=255)
    cat_description = models.CharField(max_length=255)

    def __str__(self):
        return self.cat_name

### Has many to one relationships with categories
class Topic(models.Model):
    topic_subject = models.CharField(max_length=255)
    topic_content = models.TextField()
    topic_date = models.DateTimeField('time sent')
    topic_by = models.ForeignKey(User, on_delete=models.CASCADE)
    topic_cat = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.topic_subject

class Reply(models.Model):
    reply_content = models.TextField()
    reply_date = models.DateTimeField('time sent')
    reply_by = models.ForeignKey(User, on_delete=models.CASCADE)
    reply_topic = models.ForeignKey(Topic, on_delete=models.CASCADE)

    def __str__(self):
        return self.reply_content