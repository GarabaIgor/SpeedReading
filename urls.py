from django.conf.urls.defaults import patterns, include, url
from SpeedReading.exercises import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	# (r'^base/$',views.base_exercise),
    (r'^home/$',views.home_page),
	(r'^schulte/$',views.schulte_table_about),
    (r'^schulte_table_html/$',views.schulte_table_html),
	# (r'^schulte_about/$',views.schulte_table_about),
    (r'^field_of_view_exercise_about/$',views.field_of_view_exercise_about),
    (r'^get_schulte_table_result/$',views.schulte_table_result),
    (r'^green_point/$',views.green_point),
    (r'^green_point_html/$',views.green_point_html),
    (r'^green_point_result/$',views.green_point_result),
    # (r'^green_point_about/$',views.green_point_about),
    (r'^storm_about/$',views.storm_about),
    (r'^storm/$',views.storm),
    (r'^vertical_about/$',views.vertical_about),
    (r'^vertical/$',views.vertical),
    (r'^attention_letters/$',views.attention_letters),
    (r'^get_attention_letters_result/$',views.get_attention_letters_result),
    (r'^attention_letters_json/$',views.attention_letters_json),
   # (r'^attention_letters_html/$',views.attention_letters_html),
    (r'^attention_letters_html_from_modal/$',views.attention_letters_html_from_modal),
    (r'^double_images/$',views.double_images),
    (r'^double_images_json/$',views.double_images_json),
        
    (r'^summ/$',views.summ),
    # Examples:
    # url(r'^$', 'SpeedReading.views.home', name='home'),
    # url(r'^SpeedReading/', include('SpeedReading.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
