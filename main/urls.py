from django.contrib import admin
from django.urls import path, include, re_path

from django.conf import settings
from django.conf.urls.static import static

from custhome.views import HomeMainView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeMainView.as_view(), name='home'),
    path('account/', include('account.urls')),
    path('address/', include('address.urls')),
    path('bag/', include('bag.urls')),
    path('category/', include('category.urls')),
    path('order/', include('order.urls')),
    path('payment/', include('payment.urls')),
    path('product/', include('product.urls')),
    path('search/', include('search.urls')),
    path('wishlist/', include('wishlist.urls')),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
