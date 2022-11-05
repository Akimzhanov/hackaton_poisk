from django.urls import path
from .views import(
    RegistrationView,
    AccountActivationView,
    DeleteAccountView,
    LogoutView,
    SetRestoredPasswordView,
    RestorePasswordView,
    ChangePasswordView
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView
)



urlpatterns = [
    path('register/', RegistrationView.as_view(), name='registration'),
    path('activate/<str:activation_code>/', AccountActivationView.as_view(), name='activation'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('delete-account/', DeleteAccountView.as_view(), name='delete_account'),
    path('logout/', LogoutView.as_view(), name='log_out'),
    path('change-password/', ChangePasswordView.as_view(), name='change_password'),
    path('restore-password/', RestorePasswordView.as_view(), name='restore_password'),
    path('set-restored-password/', SetRestoredPasswordView.as_view(), name='set_restored_password'),



]

















