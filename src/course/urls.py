from django.urls import path
from django.conf.urls import url
from django.views.static import serve
from django.conf import settings


from . import views

app_name='course'
urlpatterns = [
    path('levels', views.levels, name = 'levels' ),
    path('<int:id>', views.get_subjects, name = 'get_subjects' ),
    path('<int:id>/lectures', views.get_lectures, name = 'get_lectures' ),
    url(r'^download/(?P<path>.*)$', serve, {'document root': settings.MEDIA_ROOT}),
    # path('some-view', views.some_view, name = 'some_view' ),

]