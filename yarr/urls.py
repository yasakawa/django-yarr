from django.conf.urls import url
from yarr import views
from yarr.constants import ENTRY_UNREAD, ENTRY_READ, ENTRY_SAVED

urlpatterns = [
    url(r'^$', views.home, name="yarr-home"),
    url(r'^all/$', views.list_entries,name="yarr-list_all",),
    url(r'^unread/$', views.list_entries,{'state': ENTRY_UNREAD},name="yarr-list_unread",),
    url(r'^saved/$', views.list_entries,{'state': ENTRY_SAVED},name="yarr-list_saved",),

    # Feed views
    url(r'^all/(?P<feed_pk>\d+)/$', views.list_entries,name="yarr-list_all",),
    url(r'^unread/(?P<feed_pk>\d+)/$', views.list_entries,{'state': ENTRY_UNREAD},name="yarr-list_unread"),
    url(r'^saved/(?P<feed_pk>\d+)/$', views.list_entries,{'state': ENTRY_SAVED},name="yarr-list_saved",),

    # Feed management
    url(r'^feeds/$', views.feeds,name="yarr-feeds"),
    url(r'^feeds/add/$', views.feed_form,name="yarr-feed_add",),
    url(r'^feeds/(?P<feed_pk>\d+)/$', views.feed_form,name="yarr-feed_edit",),
    url(r'^feeds/(?P<feed_pk>\d+)/delete/$', views.feed_delete, name="yarr-feed_delete",),
    url(r'^feeds/export/$', views.feeds_export,name="yarr-feeds_export",),

    # Flag management without javascript
    url(r'^state/read/all/$', views.entry_state,{'state': ENTRY_READ, 'if_state': ENTRY_UNREAD},name="yarr-mark_all_read",),
    url(r'^state/read/feed/(?P<feed_pk>\d+)/$', views.entry_state,{'state': ENTRY_READ},name="yarr-mark_feed_read"),
    url(r'^state/read/entry/(?P<entry_pk>\d+)/$', views.entry_state,{'state': ENTRY_READ},name="yarr-mark_read"),
    
    url(r'^state/unread/entry/(?P<entry_pk>\d+)/$', views.entry_state,{'state': ENTRY_UNREAD},name="yarr-mark_unread",),
    url(r'^state/save/entry/(?P<entry_pk>\d+)/$', views.entry_state,{'state': ENTRY_SAVED}, name="yarr-mark_saved"),

    # JSON API
    url(r'^api/$', 'api_base', name='yarr-api_base'),
    url(r'^api/feed/get/$', 'api_feed_get', name='yarr-api_feed_get'),
    url(r'^api/feed/pks/$', 'api_feed_pks_get', name='yarr-api_feed_pks_get'),
    url(r'^api/entry/get/$', 'api_entry_get', name='yarr-api_entry_get'),
    url(r'^api/entry/set/$', 'api_entry_set', name='yarr-api_entry_set'),
]
