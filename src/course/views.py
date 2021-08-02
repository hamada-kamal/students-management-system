from django.shortcuts import render
from .models import *
import os
from django.conf import settings
from django.http import HttpResponse, Http404
# Create your views here.

def levels(request):
    levels = Level.objects.all()
    return render(request,'course/levels.html',{'levels': levels})



def get_subjects(request,id):
    subjects = Subject.objects.filter(level_id=id)
    level = Level.objects.get(id=id)
    subject_semester1 = []
    subject_semester2 = []
    for subject in subjects:
        if subject.semester == "semester1":
            subject_semester1.append(subject)
        else:
            subject_semester2.append(subject)
    for s2 in subject_semester2:
        print(s2)
    return render(request,'course/subjects.html',{'subjects': subjects, 'level': level, 'subject_semester1': subject_semester1, 'subject_semester2': subject_semester2})




def get_lectures(request,id):
    all_lectures = Lecture.objects.filter(belongs_to_id=id)
    subject = Subject.objects.get(id=id)
    lectures = [] 
    sections = [] 
    labs = []
    for l in all_lectures:
        if l.type=='lecture':
            lectures.append(l)
        elif l.type=='section':
            sections.append(l)
        else:
            labs.append(l)
    return render(request, 'course/lectures.html', {'lectures': lectures, 'sections': sections,'labs': labs, 'subject': subject}) 




def download(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/adminupload")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404


import csv
from django.http import HttpResponse

# def some_view(request):
#     # Create the HttpResponse object with the appropriate CSV header.
#     response = HttpResponse(
#         content_type='text/csv',
#         headers={'Content-Disposition': 'attachment; filename="somefilename.csv"'},
#     )

#     writer = csv.writer(response)
#     writer.writerow(['First row', 'Foo', 'Bar', 'Baz'])
#     writer.writerow(['Second row', 'A', 'B', 'C', '"Testing"', "Here's a quote"])
#     writer.writerow(['Second row', 'A', 'B', 'C', '"Testing"', "Here's a quote"])

#     return response