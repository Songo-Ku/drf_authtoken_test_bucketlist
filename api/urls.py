from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns

from rest_framework.authtoken import views
from .views import CreateView, DetailsView, UserCreate, CustomAuthToken, ListUsers, LoginView
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = {
    path('bucketlists/', CreateView.as_view(), name="create"),
    path('bucketlists/<int:pk>/', DetailsView.as_view(), name="details"),
    path('auth/', include('rest_framework.urls'), name='rest_framework'),

    path('get-token/', obtain_auth_token),

    path("api/users/", ListUsers.as_view(), name="users-list"),
    path("api/token/auth", CustomAuthToken.as_view()),  # to jest customowy auth ktory daje wiecej pol

    path("login/", views.obtain_auth_token, name="login"),
    path("logout/", views.obtain_auth_token, name="logout"),
    path("login-password/", LoginView.as_view(), name="login-password"),

    path("users/", UserCreate.as_view(), name="user_create"),

    # path('users/', UserView.as_view(), name="users"),
    # path('users/<int:pk>/', UserDetailsView.as_view(), name="user_details"),
}

urlpatterns = format_suffix_patterns(urlpatterns)