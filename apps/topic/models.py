from django.contrib.auth.models import User
from django.db import models
from common.models import BaseModel


class TopicModel(BaseModel):
    title = models.CharField(max_length=256)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    content = models.TextField()
    node_id = models.ForeignKey(
        'TopicNodeModel', on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'topic'
        ordering = ('-updated_time',)

    def __str__(self):
        return self.title


class TopicCommentModel(BaseModel):
    topic = models.ForeignKey('TopicModel', on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    content = models.TextField()

    class Meta:
        db_table = 'topic_comment'
        ordering = ('created_time',)

    def __str__(self):
        return self.topic.title


class TopicNodeModel(BaseModel):
    name = models.CharField(max_length=60, null=True)
    create_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'topic_node'
        ordering = ('created_time',)
