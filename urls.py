from django.conf.urls import patterns

urlpatterns = patterns('',
    (r'^$','pdfs.views.index'),
)

