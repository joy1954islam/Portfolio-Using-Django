from django.shortcuts import render
from .models import Education,Language,Basic_Information
# Create your views here.


def Home(request):
    basic_information = Basic_Information.objects.all()
    education = Education.objects.all()
    context = {
        'basic_information': basic_information,
        'education':education,

    }
    return render(request,'index.html',context)