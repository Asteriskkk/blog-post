from rest_framework.generics import ListAPIView
from comment.models import Comment
from.serializers import CommentSerializer
class CommentView(ListAPIView):
	queryset = Comment.objects.all()
	serializer_class = CommentSerializer
