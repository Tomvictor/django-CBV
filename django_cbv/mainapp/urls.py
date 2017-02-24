from django.conf.urls import url,include
from mainapp import views

urlpatterns = [
    url(r'^$',views.home_page.as_view(), name='home'),
    url(r'^list$',views.profile_list_view.as_view(), name='list'),
    url(r'^(?P<pk>[-\w]+)/$',views.profile_detail_view.as_view(), name='detail'),
]
