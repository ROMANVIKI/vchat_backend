from rest_framework import routers
from custom_users.viewsets import UserViewSet
from core.auth.viewsets.register import RegisterViewSet
from core.auth.viewsets.login import LoginViewSet

from core.auth.viewsets.refresh import RefreshViewSet


from core.post.viewsets import PostViewset

router = routers.SimpleRouter()


router.register(r'user', UserViewSet, basename='user')
router.register(r'auth/register', RegisterViewSet, basename='auth-register')
router.register(r'auth/login', LoginViewSet, basename='auth-login')

router.register(r'auth/refresh', RefreshViewSet, basename='auth-refresh')

router.register(r'post', PostViewset, basename='post')


urlpatterns = [
    *router.urls,
]