from mptt.admin import MPTTModelAdmin

from omniport.admin.site import omnipotence

from comments.models import Comment


omnipotence.register(Comment, MPTTModelAdmin)
