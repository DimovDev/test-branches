# Django viewset
from django.conf.urls import url, include


# registriraj router
from rest_framework.routers import DefaultRouter

from api.user import views
from api.all_product import views as all_product_views
from api.user.views import LogoutApiView

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')
router.register('profile', views.UserProfileViewSet)  # ne treba base_name jer Django rest_framework skuzi
router.register('login', views.LoginViewSet, base_name='login')
# router.register('logout', views.logout, base_name='logout')
router.register('feed', views.UserProfileFeedViewSet)
router.register('messages_sent', views.SentMessagesViewSet, base_name='messages_sent')
router.register('messages_received', views.ReceivedMessagesViewSet, base_name='messages_received')
router.register('my_products', all_product_views.MyProductViewSet, base_name='my_products')
router.register('category', all_product_views.MyCategoryViewSet, base_name='category')
router.register('all_products', all_product_views.AllProductViewSet, base_name='all_products')
router.register('location', all_product_views.MyLocationsViewSet, base_name='location')



urlpatterns = [
    url(r'^hello-view/', views.HelloApiView.as_view()),
    url(r'^logout/', views.LogoutApiView.as_view()),
    # url(r'^logout/', Logout.as_view()),
    url(r'', include(router.urls)),

]
