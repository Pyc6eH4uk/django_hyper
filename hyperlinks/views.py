from django.shortcuts import render, get_object_or_404
from hyperlinks.models import Subject, Student


def index(request):
    subjects = Subject.objects.all()
    return render(request, 'index.html', {'subjects': subjects})


def object_info(request, subject_id):
    subject = get_object_or_404(Subject, id=subject_id)
    students = Student.objects.filter(subject=subject_id)
    return render(request, 'subject.html', {'students': students, 'subject_name': subject.title})

