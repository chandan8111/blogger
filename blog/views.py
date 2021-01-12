from django.shortcuts import render, HttpResponse

# Create your views here.
def blogHome(request):
    return HttpResponse("Tis is blog.")
    

def blogPost(request, slug):
    return HttpResponse(f"Tis is blog.{slug}")