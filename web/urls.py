from django.conf.urls import url
from web import views

urlpatterns = [
    url(r'^$', views.landing),

    url(r'^contact$', views.contact),
    url(r'^about$', views.about),

    url(r'^services/staff$', views.staff_service),
    url(r'^services/client$', views.client_service),
    url(r'^services/appointment$', views.appointment_service),
    url(r'^services/class$', views.class_service),
    url(r'^services/site$', views.site_service),
    url(r'^services/sale$', views.sale_service),
    url(r'^services/clientsreport$', views.clients_report),

    url(r'^login$', views.log_in),
    url(r'^logout$', views.log_out),

    url(r'^join$', views.create_account),
    url(r'^profile$', views.profile),

    
]