from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import(
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),

    #Rutas para autenticación con JWT

    # Es la pantalla de Login. Recibe usuario/contraseña y te devuelve el Par (El de acceso y el de refresco).
    # .as_view() es un traductor que convierte la clase en algo que la URL puede leer
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # Es la ventanilla de cambio. Recibe un Token de Refresco viejo y te devuelve un Token de Acceso nuevo.
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # urls de Usuarios
    path('api/usuarios/', include('usuarios.urls')),
]
