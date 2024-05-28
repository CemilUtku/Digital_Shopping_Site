from django.contrib import admin
from django.urls import path, include
from simple_shopping_site import views as simple_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', simple_views.home, name='home'),
    path('products/', simple_views.products, name='products'),
    path('process_order/', simple_views.process_order, name='process_order'),
    path('list_orders/', simple_views.list_orders, name='list_orders'),
    path('create_product/', simple_views.create_product, name='create_product'),
    path('create_customer/', simple_views.create_customer, name='create_customer'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('list_customers/', simple_views.list_customers, name='list_customers'),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', simple_views.signup, name='signup'),
]