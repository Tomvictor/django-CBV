from django.conf.urls import url,include
from mainapp import views

urlpatterns = [
    url(r'^$',views.home, name='home'),
]
