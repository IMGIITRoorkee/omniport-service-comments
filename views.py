from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from comments.models import Comment
from comments.serializers import CommentSerializer


class CommentViewSet(ModelViewSet):
    """
    The view for Comment model CRUD operations
    """

    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, ]
    http_method_names = [
        'get',
        'post',
        'patch',
        'delete',
    ]

    def get_queryset(self):
        """
        This function returns the comments corresponding to the user making the
        request
        :return: the queryset containing the comments by the user
        """

        return Comment.objects.filter(commenter=self.request.user.person)

    def perform_create(self, serializer):
        """
        Add person as the commenter while creating the comment
        :param serializer: the serializer object
        """

        person = self.request.user.person
        serializer.save(commenter=person)

