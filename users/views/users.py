from rest_framework import generics, permissions
from django.contrib.auth import get_user_model
from users.serializers.users import UserSerializer

User = get_user_model()

class UserProfileView(generics.RetrieveUpdateAPIView):
    """
    Permite a un usuario obtener y actualizar su perfil.
    Solo accesible para usuarios autenticados.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user
