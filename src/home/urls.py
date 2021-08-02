from django.urls import path

from . import views

app_name='home'
urlpatterns = [
    path('', views.index, name = 'index' ),
    path('complaints/add', views.complaints, name = 'complaints' ),
    path('registration', views.registration, name = 'registration' ),
    path('show-registerd-subject', views.show_registerd_subject, name = 'registerd_subject' ),
    path('delete-registerd-subject', views.delete_registerd_subject, name = 'delete_subject' ),
]