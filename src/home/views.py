from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .forms import ComplaintForm
from django.urls import reverse
from django.contrib import messages
from course.models import Subject
from .models import Registraion
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
import json



@login_required
def index(request):
    return render(request, 'home/index.html', {})




def complaints(request):
    if request.method == 'POST':
        form = ComplaintForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Your Complaint Send Successfully')
            return redirect(reverse('home:index'))
    else:
        form = ComplaintForm()
    return render(request, 'home/complaints.html', {'form':form})


def registration(request):
    primary_subject_s1 = Subject.objects.filter(level_id=1, semester = 'semester1')
    primary_subject_s2 = Subject.objects.filter(level_id=1, semester = 'semester2')

    level_one_subject_s1 = Subject.objects.filter(level_id=2, semester = 'semester1')
    level_one_subject_s2 = Subject.objects.filter(level_id=2, semester = 'semester2')

    level_two_subject_s1 = Subject.objects.filter(level_id=3, semester = 'semester1')
    level_two_subject_s2 = Subject.objects.filter(level_id=3, semester = 'semester2')

    level_three_subject_s1 = Subject.objects.filter(level_id=4, semester = 'semester1')
    level_three_subject_s2 = Subject.objects.filter(level_id=4, semester = 'semester2')

    level_four_subject_s1 = Subject.objects.filter(level_id=5, semester = 'semester1')
    level_four_subject_s2 = Subject.objects.filter(level_id=5, semester = 'semester2')

    if request.method == 'POST':
        subject_code = request.POST['code']
        if subject_code:
            subject = Subject.objects.get(code = subject_code)
            register_instance = get_object_or_404(Registraion, user = request.user)
            if subject not in register_instance.subjects.all():
                register_instance.subjects.add(subject)
                messages.success(request,'subject added successfully')
                return redirect('/home/registration')
            else:
                messages.success(request,'subject allredy added')
        else:
            messages.success(request,'please enter valid code')
            return redirect(reverse('home:registration'))
    return render(request, 'home/registration.html', {
        'primary_subject_s1':primary_subject_s1,
        'primary_subject_s2':primary_subject_s2,
        'level_one_subject_s1':level_one_subject_s1, 
        'level_one_subject_s2':level_one_subject_s2,
        'level_two_subject_s1':level_two_subject_s1, 
        'level_two_subject_s2':level_two_subject_s2,
        'level_three_subject_s1':level_three_subject_s1, 
        'level_three_subject_s2':level_three_subject_s2,
        'level_four_subject_s1':level_four_subject_s1, 
        'level_four_subject_s2':level_four_subject_s2, 
        })



def show_registerd_subject(request):
    register_instance = get_object_or_404(Registraion, user = request.user)
    # subject = Subject.objects.g
    return render(request, 'home/show_registerd_subject.html', {'register_instance':register_instance})


def delete_registerd_subject(request):
    data = json.loads(request.body)
    subjectId = data['subjectId']
    action = data['action']
    register_instance = get_object_or_404(Registraion, user = request.user)
    subject = Subject.objects.get(id=subjectId)
    if action=='remove':
        register_instance.subjects.remove(subject)
        # return redirect('/home/show-registerd-subject')
    return JsonResponse('subject deleted',safe=False)

