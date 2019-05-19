from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticated

from comments.models import Comment
from comments.serializers import CommentSerializer


class CommentViewSet(
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):
    """
    View for CUD operations of a comment
    Never list or retrieve comments, always serialize in parent model
    """

    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, ]

    def get_queryset(self):
        """
        Returns the comments written by the user making the request
        :return: the queryset containing the comments by the user
        """

        return Comment.objects.filter(commenter=self.request.person)

    def perform_create(self, serializer):
        """
        Add person as the commenter while creating the comment
        :param serializer: the serializer object with the populated data
        """

        person = self.request.person
        serializer.save(commenter=person)
