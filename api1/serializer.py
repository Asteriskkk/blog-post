from rest_framework.serializers import ModelSerializer, HyperlinkedIdentityField, SerializerMethodField
from post.models import post


class PostListSerializer(ModelSerializer):
    url = HyperlinkedIdentityField(view_name='post_api:detail')
    user = SerializerMethodField()
    image = SerializerMethodField()
    # timestamp = SerializerMethodField()


    class Meta:
        model = post
        fields = ['url', 'id', 'user', 'title', 'context', 'image',]

    def get_user(self, obj):
        return str(obj.user.id)

    def get_image(self, obj):
        try:
            image = obj.image.url
        except:
            image = None
        return image

    # def get_timestamp(self,obj):
    #     return str(obj.timestamp.DateTimeField)


class PostDetailSerializer(ModelSerializer):
    delete = HyperlinkedIdentityField(view_name='post_api:delete')

    class Meta:
        model = post
        fields = ['delete', 'id', 'user', 'title', 'context']


class PostDeleteSerializer(ModelSerializer):
    class Meta:
        model = post
        fields = ['id', 'user', 'title', 'context']


class PostUpdateSerializer(ModelSerializer):
    class Meta:
        model = post
        fields = ['id', 'user', 'title', 'context']
