from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'dwebsite/home.html', {})

def contact(request):
    return render(request, 'dwebsite/contact.html', {})