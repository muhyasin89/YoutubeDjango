
from django.urls import path, include
from rest_framework import routers
from api.views.users import UserViewSet
from api.views.register import RegisterUserAPIView


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'/users', UserViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('/register/',RegisterUserAPIView.as_view(), name="register"),
    path('/auth/', include('djoser.urls.authtoken')),
]