from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
def home(request):
    if request.method == "POST":
        app_department = request.POST['app-department']
        app_name = request.POST['app-name']
        app_email = request.POST['app-email']
        app_date = request.POST['app-date']
        app_time = request.POST['app-time']
        app_phone = request.POST['app-phone']

        # send an email to the dentist
        send_mail(
            'Appointment request  from ' + app_name, # subject
            'Requested date: ' + app_date + ' ' + 'requested time: ' + app_time + ' ' + 'Phone number: ' + app_phone, # message
            app_email, # from email
            ['dentist@gmail.com'], # To Email. dummy email!
        )

        return render(request, 'dwebsite/home.html', {'app_name': app_name, 'app_date': app_date, 'app_time':app_time})

    else:
        return render(request, 'dwebsite/home.html', {})


def services(request):
    return render(request, 'dwebsite/services.html', {})

def doctors(request):
    return render(request, 'dwebsite/doctors.html', {})

def blog(request):
    return render(request, 'dwebsite/blog.html', {})

def about(request):
    return render(request, 'dwebsite/about.html', {})


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