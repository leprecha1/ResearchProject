from django.conf.urls import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'account.views.home', name='home'),
    url(r'admin/(.*)$', 'account.views.admin', name='admin'),
    url(r'logout/(.*)$', 'account.views.logoff', name='logout'),
    url(r'login/(.*)$', 'account.views.loginPage', name='login'),
    url(r'signup/(.*)$', 'account.views.signup', name='signup'),
    url(r'home/(.*)$', 'account.views.userhome', name='userhome'),
    url(r'research/$', 'account.views.research_list', name='research_list'),
    url(r'research/new$', 'account.views.research_new', name='research_new'),
    url(r'research/(.*)/edit$', 'account.views.research_edit', name='research_edit'),
    url(r'research/[0-9]$', 'account.views.research_answer', name='research_answer'),
    #url(r'research/(.*)/view$', 'account.views.research_view', name='research_view'),
    #url(r'research/(.*)/graph$', 'account.views.research_graph', name='research_graph'),
    (r'^assets/(.*)$', 'django.views.static.serve',
                       {'document_root': settings.MEDIA_ROOT}),
)
