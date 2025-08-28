from rest_framework import permissions

class IsOwnerOrReadOnlyDetailAPIView(permissions.BasePermission):
  """
  Permite edición/borrado solo al dueño del objeto.
  Lectura para todos.
  """

  def has_object_permission(self, request, view, obj):
    if request.method in permissions.SAFE_METHODS:
      return True

    return obj.user == request.user

class CanCreateContent(permissions.BasePermission):
  """
  Permite crear posts o comentarios propios
  """

  def has_permission(self, request, view):
    return
