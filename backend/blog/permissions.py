from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS: # (GET, HEAD, OPTIONS)
            return True
        
        return obj.author == request.user
    

class CanCreateIfAuthenticatedAndAlmostCanRead(permissions.BasePermission):
    def has_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS: # (GET, HEAD, OPTIONS)
            return True
        elif request.user.is_authenticated:
            return True
        else:
            return False