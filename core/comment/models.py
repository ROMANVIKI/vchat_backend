from django.db import models
from core.abstract.models import AbstractManager, AbstractModel
from core.post.models import Post
from custom_users.models import User

class CommentManager(AbstractManager):
    pass


class Comment(AbstractModel):
    post = models.ForeignKey("core_post.Post", on_delete=models.PROTECT)
    author = models.ForeignKey("custom_users.User", on_delete=models.PROTECT)

    body = models.TextField()

    edited = models.BooleanField(default=False)

    objects = CommentManager()

    def __str__(self):
        return self.author.name
    