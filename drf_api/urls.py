from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from rest_framework.documentation import include_docs_urls

from drf_api import views


urlpatterns = [
    path('admin/', admin.site.urls),
]

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('docs/', include_docs_urls(title='API v1.0')),
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('companies/', views.CompanyList.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
