from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from .views import RegisterView


router = DefaultRouter()
router.register(r'menu', views.MenuViewSet)
router.register(r'booking', views.BookingViewSet)


urlpatterns = [
    path('', views.index, name='index'),
    path('auth/', include('rest_framework.urls')),
    path('', include(router.urls)),
    path('menu/<int:pk>/', views.SingleMenuItemView.as_view(), name='single-menu-item'),
    path('message/', views.msg),
    path('api-token-auth/', obtain_auth_token),
    path('register/', RegisterView.as_view(), name='register'),
]
