from django.urls import path, include
from kalamlabs import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('register',views.Register,basename='register')
# router.register('payment',views.payment(),basename='payment')

urlpatterns = [
    path('payment/',views.payment),
    path('verify_signature/',views.verifySignature),
    path('',include(router.urls))
]