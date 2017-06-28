from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.contenttypes.models import ContentType
from comment.models import Comment
from django.conf import settings


class post(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,default=1)
    title=models.CharField(max_length=200)
    image=models.FileField(null=True,blank=True)
    context=models.TextField()
    update=models.DateTimeField(auto_now=True,auto_now_add=False)
    timestamp=models.DateTimeField(auto_now=False,auto_now_add=True)



    def __str__(self):
        return self.title

    def piyush(self):
        return reverse("post:detail", kwargs={"id":self.id})

    @property
    def comments(self):
        instance=self
        qs=Comment.objects.filter_by_instance(instance)
        return qs

    @property
    def get_content_type(self):
        instance = self
        content_type = ContentType.objects.get_for_model(instance.__class__)
        return content_type