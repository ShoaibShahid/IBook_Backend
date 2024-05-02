
from django.urls import path, include
from ibook_apis.views import UserCreateView,LoginUserView,ProjectCreateView,getUserProjectsView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('user/login', LoginUserView.as_view(), name='login user'),
    path('user/create', UserCreateView.as_view(), name= "user create"),
    path('user/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('project/create', ProjectCreateView.as_view(), name= "project create"),
    path('project/list', getUserProjectsView, name= "project list"),
]
