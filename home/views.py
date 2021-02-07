from django.shortcuts import render, HttpResponse, redirect
from home.models import Contact
from django.contrib import messages
from blog.models import Post
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

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

def search(request):
    query = request.GET['query']
    if len(query)>200:
        allpost = Post.objects.none()
    else:
        allposttitle = Post.objects.filter(title__icontains=query)
        allpostcontent = Post.objects.filter(content__icontains=query)
        allpost = allposttitle.union(allpostcontent)

    if allpost.count() == 0:
        messages.warning(request, "No search result found. Please refine your query.")
        
    context = {"allpost": allpost, 'query':query}
    return render(request, 'home/search.html', context)

def handleSignup(request):
    if request.method == 'POST':
        # Get the post parameters
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        Email = request.POST['email']
        email = Email.lower()
        password = request.POST['password']
        Password = request.POST['Password']
        # Check in input error
        if len(username) < 3:
            messages.error(request, "Username must be above 4 character.")
            return redirect("/")
        if not username.isalnum():
            messages.error(request, "Username should only contain letter or number")
            return redirect("/")
        if password != Password:
            messages.error(request, "Passwords do not match.")
            return redirect("/")
        # Create User
        myuser = User.objects.create_user(username, email, password)
        myuser.first_name = firstname
        myuser.last_name = lastname
        myuser.save()
        messages.success(request, "Your blogger account has been successfully created")
        return redirect("/")

    else:
        return HttpResponse('404 - Not Found')

def handleLogin(request):
    if request.method == 'POST':
        loginId = request.POST['loginid']
        loginPassword = request.POST['loginpassword']
        user = authenticate(username=loginId, password=loginPassword)
        if user is not None:
            login(request, user)
            messages.success(request, "Sucessfully loged in")
            return redirect("/")  
        else:
            messages.error(request, "Invalid Credentials, Please try again")
            return redirect("/")   
    
    return HttpResponse('404 - Not Found')

def handleLogout(request):
    if request.method == 'POST':
        logout(request)
        messages.warning(request, "Successfully logged out")
        return redirect("/")
    
    return HttpResponse('404 - Not Found')