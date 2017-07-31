from django.conf.urls import url, include
from django.contrib import admin
from tasks import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.user_page_view, name='user_page'),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^accounts/sign_up/$', views.sign_up_view, name='sign_up'),
    url(r'^add_task/$', views.add_task_view, name='add_task'),
    url(r'^edit/([0-9]+)/$', views.edit_task_view, name='edit_task'),
]
