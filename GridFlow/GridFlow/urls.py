"""GridFlow URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

admin.site.site_header = "GridFlow Administration"
admin.site.site_title = "GridFlow Site Admin"
admin.site.index_title = "GridFlow Admin Panel"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/store/', include('store.api.urls', 'store-api')),
    path('api/shop/', include('shop.api.urls', 'shop-api')),
    path('api/gallery/', include('gallery.api.urls', 'gallery-api')),
    path('api/order/', include('order.api.urls', 'order-api')),
    path('api/accounting/', include('accounting.api.urls', 'accounting-api')),
    path('api/messenger/', include('messenger.api.urls', 'messenger-api')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('shop/', include('shop.urls')),
    path('messenger/', include('messenger.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
