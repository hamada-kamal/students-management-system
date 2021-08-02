from annoying.decorators import render_to
from django.http import HttpResponse
from pyzbar import pyzbar
import qrcode
import cv2
import csv
from accounts.models import Profile
from django import template
from django.urls import reverse
register = template.Library()



my_list = []


def read_barcode(frame):
    barcodes = pyzbar.decode(frame)
    for barcode in barcodes:
        x , y , w , h = barcode.rect
        barcode_info = barcode.data.decode ('utf-8')
        
        cv2.rectangle( frame , ( x , y ) , ( x + w , y + h ) , ( 0 , 255 , 0 ) , 2 )
        # 2
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText( frame , barcode_info , ( x + 6 , y - 6 ) , font , 2.0 , ( 255 , 255 , 255 ) , 1 )
        my_list.append(barcode_info)    
    return frame



def index(request):
    res = []
    camera = cv2.VideoCapture(0)
    ret , frame = camera.read()
    while ret:
        ret , frame = camera.read()
        frame = read_barcode(frame)
        cv2.imshow( 'QR code reader'+ ' ' + '(press Esc to exit)' , frame )
        for i in my_list:
            if i not in res:
                res.append(i)

        if cv2.waitKey(1) & 0xFF == 27:
            break
    camera.release()
    cv2.destroyAllWindows()
    response = HttpResponse(
    content_type='text/csv',
    headers={'Content-Disposition': 'attachment; filename="attendance.csv"'},
        )

    writer = csv.writer(response)
    for i in res:
        writer.writerow([i])
    return response

def generate_qr_code(data, size=10, border=0):
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L,
                       box_size=size, border=border)
    qr.add_data(data)
    qr.make(fit=True)
    return qr.make_image()

@render_to()
def return_qr(request):
    profile = Profile.objects.get(user=request.user)
    qr = generate_qr_code(profile.user.first_name + ' ' + profile.user.last_name, 10, 2)
    response = HttpResponse(content_type="image/png")
    qr.save(response, "PNG")
    return response

@register.inclusion_tag('attendance/qrcode_maker.html', takes_context=True)
def get_qrcode_image(context, text, size):
    url = reverse('/home/')
    return {'url': url, 'text': text, 'size': size}