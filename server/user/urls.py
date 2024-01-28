from django.urls import path, include

from user.views import ListRegisterView, LoginView, UserDeleteView

urlpatterns = [
    path("api/users", ListRegisterView.as_view(), name="user_list_register"),
    path("api/login", LoginView.as_view(), name="api_token_auth"),
    path("api/users/<str:email>", UserDeleteView.as_view(), name="user_delete"),
]
