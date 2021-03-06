from django.conf.urls import patterns, include, url
from django.contrib import admin
from kandoo.views import SignUpView

urlpatterns = patterns('',
    url(r'^$', 'kandoo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': 'home'}, name='log_out'),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'create_account.html '}, name='log_in'),
    url(r'^create_account/$', SignUpView.as_view(), name='create_account'),
    url(r'^create_account2/$', 'kandoo.views.user_creation', name='user_creation'),
    url(r'^user_page/$', 'kandoo.views.user_page', name='user_page')
)
