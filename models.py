import swapper
from mptt.models import MPTTModel, TreeForeignKey

from django.db import models

from kernel.utils.upload_to import UploadTo


class Comment(MPTTModel):
    """
    This class holds information about a comment
    """

    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)

    text = models.TextField()

    parent = TreeForeignKey(
        to='self',
        on_delete=models.CASCADE,
        related_name='children',
        null=True,
        blank=True,
    )

    commenter = models.ForeignKey(
        to=swapper.get_model_name('kernel', 'Person'),
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    attachment = models.FileField(
        upload_to=UploadTo('comments', 'attachments'),
        null=True,
        blank=True,
    )

    def __str__(self):
        """
        Return the string representation of the model
        :return: the string representation of the model
        """

        text = self.text
        commenter = self.commenter

        return f'{commenter}: {text}'

