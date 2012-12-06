from django.conf.urls.defaults import patterns, include, url
from SpeedReading.exercises import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	(r'^base/$',views.base_exercise),
	(r'^schulte/$',views.schulte_table),
	(r'^schulte_about/$',views.schulte_table_about),
    (r'^field_of_view_exercise_about/$',views.field_of_view_exercise_about),
    (r'^get_schulte_table_inf/$',views.schulte_table_inf),
    (r'^green_point/$',views.green_point),
    (r'^green_point_about/$',views.green_point_about),
    (r'^storm_about/$',views.storm_about),
    (r'^storm/$',views.storm),
    (r'^vertical_about/$',views.vertical_about),
    (r'^vertical/$',views.vertical),
    (r'^attention_letters/$',views.attention_letters),
    (r'^attention_letters_json/$',views.attention_letters_json),
    (r'^summ/$',views.summ),
    # Examples:
    # url(r'^$', 'SpeedReading.views.home', name='home'),
    # url(r'^SpeedReading/', include('SpeedReading.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
