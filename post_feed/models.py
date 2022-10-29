from django.db import models
from account.models import User


# Default BaseModel
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null = True)
    
    class Meta:
        abstract = True

# Create Post Feed
class Post(models.Model):
	owner = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
	content = models.CharField(max_length=255, blank=True)

	def __str__(self):
		return self.content


# Create Comment section
class Comments(models.Model):
	owner = models.ForeignKey(User, related_name='details', on_delete=models.CASCADE)
	post = models.ForeignKey(Post, related_name='details', on_delete=models.CASCADE)
	comment = models.CharField(max_length=255)
	
	def __str__(self):
		return self.comment


# Create Like section
class Like(models.Model):
	owner = models.ForeignKey(User, related_name='likes', on_delete=models.CASCADE)
	post = models.ForeignKey(Post, related_name='likes', on_delete=models.CASCADE)
	


