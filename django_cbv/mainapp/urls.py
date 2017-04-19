from django.conf.urls import url,include
from mainapp import views

urlpatterns = [
    url(r'^$',views.profile_list_view.as_view(), name='list'),
    url(r'^(?P<pk>[-\w]+)/$',views.profile_detail_view.as_view(), name='detail'),
    url(r'^(?P<pk>[-\w]+)/$',views.ProfileUpdate.as_view(), name='edit'),
    url(r'^create$', views.profile_create_view.as_view(), name='create'),
]
