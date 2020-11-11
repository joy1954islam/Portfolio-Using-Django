from django.shortcuts import render
from .models import Education, Language, Basic_Information, Project


# Create your views here.


def Home(request):
    basic_information = Basic_Information.objects.all()
    education = Education.objects.all()
    project = Project.objects.all()
    context = {
        'basic_information': basic_information,
        'education':education,
        'project':project,

    }
    return render(request,'index.html',context)