from rest_framework.permissions import BasePermission

class IsOwner(BasePermission):
    
    message = "Access Denied"
    
    def has_object_permission(self, request, view, obj):
        print(obj.user)
        return (obj.user == request.user) or (request.user.is_superuser) # admin ya da postun sahibiyse