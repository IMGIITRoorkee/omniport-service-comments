from mptt.admin import MPTTModelAdmin

from kernel.admin.site import omnipotence

from comments.models import Comment


omnipotence.register(Comment, MPTTModelAdmin)
