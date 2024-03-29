from rest_framework.permissions import BasePermission

class IsOwner(BasePermission):
    
    message = "Access Denied"

    def has_object_permission(self, request, view, obj):
        return (obj.user == request.user) or (request.user.is_superuser)