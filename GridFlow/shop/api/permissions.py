from rest_framework.permissions import BasePermission


class AdminOnly(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.groups.filter(name="admin_only") or request.user.is_staff:
            return True
        return False


class ShopOwnerOnly(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.groups.filter(name="shop_owner_only"):
            return True
        return False


class CustomerSupportsOnly(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.groups.filter(name="customer_supports_only"):
            return True
        return False
