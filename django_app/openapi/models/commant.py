from django.conf import settings
from django.db import models

from .content import Content

__all__ = (
    'PostComment',
)


class PostComment(models.Model):
    post = models.ForeignKey(Content)
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    content = models.TextField()

    def __str__(self):
        return '{} comment (author:{})'.format(
            self.post_id,
            self.author_id
        )