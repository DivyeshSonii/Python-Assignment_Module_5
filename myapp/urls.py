from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', admin_index, name='admin_index'),
    path('add_product/', add_product, name='add_product'),
    path('edit_product/<int:pk>', edit_product , name='edit_product'),
    path('product_manager/', product_manager, name='product_manager'),
    path('searched_product/', searched_product, name='searched_product'),
    path('del_product/', del_product, name='del_product'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)