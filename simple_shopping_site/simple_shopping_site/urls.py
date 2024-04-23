from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from simple_shopping_site.views import home, create_customer, list_customers, products, create_product

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('basket/', include('basket.urls')),
    path('products/', products, name='products'),
    path('create_customer/', create_customer, name='create_customer'),
    path('list_customers/', list_customers, name='list_customers'),
    path('create_product/', create_product, name='create_product')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)