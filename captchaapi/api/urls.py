from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from api.views import *

app_name = 'api'

router = routers.DefaultRouter()


router.register(r'version', VersionViewSet, basename='Version')
router.register(r'user_activity', UserActivityViewSet, basename='UserActivity')
router.register(r'pip_message', PipMsgViewSet, basename='PipMsg')
router.register(r'classify-session', SessionClassificationViewSet, basename='classify-session')

urlpatterns = [path('', include(router.urls))]
urlpatterns += [path('token/', obtain_auth_token, name="login")]
urlpatterns += [static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)]
