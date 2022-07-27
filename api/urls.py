
from django.urls import path, include
from rest_framework import routers

from api.views.users import UserViewSet

from rest_framework.views import TokenRefreshView

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
   
    
    path('register', )
    path('auth/', include('rest_framework.urls', namespace='rest_framework'))
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]