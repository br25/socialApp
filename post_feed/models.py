from django.db import models
from account.models import User


# Default BaseModel
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True, default=None)

    class Meta:
        abstract = True


# Create Post Feed
class Post(BaseModel):
    owner = models.ForeignKey(
        User, related_name='user_posts', on_delete=models.CASCADE)
    content = models.TextField(max_length=255, blank=True)

    def __str__(self):
        return self.content


# Create Comment section
class Comment(BaseModel):
    owner = models.ForeignKey(
        User, related_name='comment_owner', on_delete=models.CASCADE)
    post = models.ForeignKey(
        Post, related_name='comments', on_delete=models.CASCADE)
    content = models.CharField(max_length=255)

    def __str__(self):
        return self.content


# Create Like section
class Like(BaseModel):
    owner = models.ForeignKey(
        User, related_name='likes', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='likes',
                             on_delete=models.CASCADE)