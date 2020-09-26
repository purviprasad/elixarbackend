from django.urls import path, include
from kalamlabs import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('register',views.Register,basename='register')
router.register('booktrial',views.BookTrial,basename='booktrial')
router.register('get_in_touch',views.GetInTouch,basename='getintouch')

urlpatterns = [
    path('payment/',views.payment),
    path('verify_signature/',views.verifySignature),
    path('send_mail/',views.send),
    path('',include(router.urls))
]