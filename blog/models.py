from django.conf import settings
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class Topic(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name=_("Author"))
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, verbose_name=_("Topic"))
    title = models.CharField(_("Title"), max_length=200)
    text = models.TextField(_("Text"))
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


