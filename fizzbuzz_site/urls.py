from django.conf.urls import include, url
from rest_framework import routers
from fizzbuzz import views


router = routers.DefaultRouter()
router.register(r'fizzbuzz', views.FizzBuzzViewSet)
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
