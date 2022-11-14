from django.urls import path
from .views import register, login, AuthenticatedUser, logout, PermissionsAPIView

urlpatterns = [
    path('register/',register),
    path('login/', login),
    path('logout/', logout),
    path('user/', AuthenticatedUser.as_view()),
    path('permissions/', PermissionsAPIView.as_view()),

]
