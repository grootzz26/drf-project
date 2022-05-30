
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import categoriesAV, productAV, AddedByAV

router = DefaultRouter()
router.register('categories', categoriesAV, basename='categories-details')
router.register('products', productAV, basename='product-details')
router.register('added_user', AddedByAV, basename='user-details')

urlpatterns = [
    path('', include(router.urls)),
]