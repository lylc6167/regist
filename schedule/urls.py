from django.urls import path
from django.conf.urls import include
from schedule import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('generator',views.GeneratorView)
router.register('schedule',views.ScheduleViewSets)

urlpatterns = [
    path('', include(router.urls)),
    ]