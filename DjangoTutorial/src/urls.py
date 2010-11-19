from django.conf.urls.defaults import include, patterns

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	(r'^polls/', include('polls.urls')),
    (r'^admin/', include(admin.site.urls)),
)
