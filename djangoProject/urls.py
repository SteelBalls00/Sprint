from django.views.generic import TemplateView
from django.contrib import admin
from django.urls import path
from rest_framework import routers
#
# router.register(r'users', views.UsersViewset)
# router.register(r'coords', views.CoordsViewset)
# router.register(r'level', views.LevelViewset)
# router.register(r'perevals', views.PerevalsViewset)
# router.register(r'images', views.ImagesViewset)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger-ui/', TemplateView.as_view(
       template_name='swagger-ui.html',
       extra_context={'schema_url':'openapi-schema'}
   ), name='swagger-ui'),
]
