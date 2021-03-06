from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'machine', views.MachineGroupViewSet)
router.register(r'member', views.MemberViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/v1/', include(router.urls)),
    url(r'^api-auth', include('rest_framework.urls', namespace='rest_framework'))
]
