from rest_framework.permissions import BasePermission


class UpdateDebtPermission(BasePermission):
    """
    Кастомный класс в котором стоят ограничения на изменения задолженности
    перед поставщиком
    """
    def has_object_permission(self, request, view, obj):
        if view.action in ['update', 'partial_update'] and 'debt' in request.data:
            return False
        return True
