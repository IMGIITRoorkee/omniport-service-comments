from django.db import models
from django.db.models import Model


class CommentableMixin(Model):
    """
    This mixin adds a tree of comments to any model
    """

    comments = models.ManyToManyField(
        to='comments.Comment',
        blank=True,
    )

    class Meta:
        """
        Meta class for CommentableMixin
        """

        abstract = True