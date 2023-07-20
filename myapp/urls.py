from . import views
from django.urls import path
from .views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('create/', CustomUserCreate.as_view(), name="create_user"),
    path('users/', Userlist.as_view(), name='users'),
    path('logout/blacklist/', BlacklistTokenUpdateView.as_view(), name='blacklist'),
    path('<int:pk>/', PostDetail.as_view(), name='detailcreate'),
    
    path('ps/', PostList.as_view(), name='suggestionlist'),
    path('ps/create/', PostCreate.as_view(), name='suggestioncreate'),

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
