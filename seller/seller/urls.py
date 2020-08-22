from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from app import apis

router = routers.DefaultRouter()
router.register(r'sellers', apis.SellerViewSet)
router.register(r'orders', apis.OrderViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('v1/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]