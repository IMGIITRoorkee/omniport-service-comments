from comments.models import Comment
from formula_one.serializers.base import ModelSerializer
from omniport.utils import switcher

AvatarSerializer = switcher.load_serializer('kernel', 'Person', 'Avatar')


class CommentSerializer(ModelSerializer):
    """
    Serializer for the Query Model
    """

    commenter = AvatarSerializer(
        read_only=True
    )

    class Meta:
        """
        Meta class for Query Serializer class
        """

        model = Comment
        exclude = (
            'datetime_modified',
            'tree_id',
            'lft',
            'rght',
            'level',
            'parent',
        )
        read_only = (
            'commenter',
            'datetime_created',
        )
        depth = 1
