from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pricing/', include('pricing.urls')),
    path('', include('pricing.urls')),
]