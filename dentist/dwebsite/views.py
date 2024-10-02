from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'dwebsite/home.html', {})

def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        return render(request, 'dwebsite/contact.html', {})

    else:
        return render(request, 'dwebsite/contact.html', {})