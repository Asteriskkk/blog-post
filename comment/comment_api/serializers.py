from rest_framework.serializers import ModelSerializer
from comment.models import Comment


class CommentSerializer(ModelSerializer):
	class Meta:
		model=Comment
		fields=['content','content_type','object_id','content_object','user']

