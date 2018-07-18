from django.urls import path
from django.conf.urls import include
from rest_framework.routers import DefaultRouter,format_suffix_patterns
from user import views


router = DefaultRouter()
router.register('account',views.AccountView)
router.register('group',views.GroupView)
router.register('profile',views.ProfileView)

#router.register('Country',views.CountryViewSet)
#router.register('Province',views.ProvinceViewSet)

router.register('register', views.RegisterView)



urlpatterns = [
    path('', include(router.urls)),
    #path('register/',views.RegisterView.as_view()),
]
