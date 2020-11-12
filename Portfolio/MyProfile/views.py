from django.core.mail import send_mail
from django.forms import forms, ModelForm
from django.shortcuts import render, redirect
from .models import Education, Language, Basic_Information, Project, Contact


# Create your views here.
class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['subject','email','phone','message',]


def Home(request):
    basic_information = Basic_Information.objects.all()
    education = Education.objects.all()
    project = Project.objects.all()
    forms = ContactForm()
    if request.method == "POST":
        forms = ContactForm(request.POST)
        if forms.is_valid():
            subject = forms.cleaned_data['subject']
            from_email = forms.cleaned_data['email']
            to_email = ['joyislam1954job@gmail.com']
            phone = forms.cleaned_data['phone']
            message = forms.cleaned_data['message']
            contact_message = "Message : %s: Phone Number : %s From Email:  %s"% (
                message,
                phone,
                from_email
                )
            send_mail(
                subject,
                contact_message,
                from_email,
                to_email,
                fail_silently=False
            )
            forms.save()
            return redirect('home')

    context = {
        'basic_information': basic_information,
        'education':education,
        'project':project,
        'forms':forms,

    }
    return render(request,'index.html',context)