from django.conf.urls import url, include
from django.contrib import admin
from tasks import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^accounts/registration', views.sign_up_view, name='registration'),
    url(r'^$', views.user_page_view, name='user_page'),
]
