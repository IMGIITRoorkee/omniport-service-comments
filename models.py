from mptt.models import MPTTModel, TreeForeignKey

from django.db import models

from kernel.models.root import Model
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

        return f'{text}'