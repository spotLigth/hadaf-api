from django.urls import path, include
from rest_framework import routers
from api import views

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users',  views.UserViewSet)
router.register(r'languages',  views.LanguageViewSet)
router.register(r'orders',  views.OrderViewSet)
router.register(r'companies',  views.CompanyViewSet)
router.register(r'contacts',  views.ContactViewSet)
router.register(r'products',  views.ProductViewSet)
router.register(r'productsimgs',  views.ProductImgViewSet)
router.register(r'categories',  views.CategoryViewSet)
router.register(r'subcategories',  views.SubcategoryViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework_api'))
]
