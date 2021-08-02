from django.urls import path

from . import views

app_name='attendance'
urlpatterns = [
    path('', views.index, name = 'take_attendance' ),
    path('get-qrcode', views.return_qr, name = 'qrcode_generater' ),
]