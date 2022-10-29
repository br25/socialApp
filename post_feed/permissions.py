from rest_framework.permissions import BasePermission


class OwnerPermission(BasePermission):

    def has_object_permission(self, request, view, post):
        return request.user.id == post.owner.id

class ConsumerPermission(BasePermission):
        
    def has_object_permission(self, request, view, post):
        return post.is_public  