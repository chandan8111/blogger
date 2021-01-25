from django.shortcuts import render, HttpResponse
from home.models import Contact
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'home/index.html')

def about(request):
    return render(request, 'home/about.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['msg']
        if len(name) < 3 or len(email) < 5 or len(phone) < 7 or  len(message) < 2 :
            messages.error(request, "Please fill the form correctly!")
        else:
            contact = Contact(name=name, email=email, phone=phone, message=message)
            contact.save()
            messages.success(request, "Your message has been sucessfuly sent!")
    return render(request, 'home/contact.html')