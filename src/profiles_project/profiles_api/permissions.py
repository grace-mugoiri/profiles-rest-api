from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """Allow user to edit their own profile."""

    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own profile."""

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id #checks if the id (person) that wants to change the profile matches the id that is currently signed/logged in


class PostOwnStatus(permissions.BasePermission):
    """Allows users to update own status"""

    def has_object_permission(self, request, view, obj):
        """Checks the user is trying to update their own status."""

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user_profile.id == request.user.id
        