from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
def home(request):
    return render(request, 'dwebsite/home.html', {})

def about(request):
    return render(request, 'dwebsite/about.html', {})

def services(request):
    return render(request, 'dwebsite/services.html', {})

def doctors(request):
    return render(request, 'dwebsite/doctors.html', {})

def blog(request):
    return render(request, 'dwebsite/blog.html', {})

def contact(request):
    if request.method == "POST":
        msg_name = request.POST['name']
        msg_email = request.POST['email']
        msg_subject = request.POST['subject']
        msg_message = request.POST['message']

        # send an email to the dentist
        send_mail(
            'message from ' + msg_name + ' ' + msg_subject, # subject
            msg_message, # message
            msg_email, # from email
            ['dentist@gmail.com'], # To Email. dummy email!
        )


        return render(request, 'dwebsite/contact.html', {'msg_name': msg_name})

    else:
        return render(request, 'dwebsite/contact.html', {})