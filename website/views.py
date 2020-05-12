from django.shortcuts import render

def home(request):
    return render(request, 'website/home.html')

def about(request):
    return render(request, 'website/about.html')

def service(request):
    return render(request, 'website/service.html')

def pricing(request):
    return render(request, 'website/pricing.html')

def blog(request):
    return render(request, 'website/blog.html')

def blog_details(request):
    return render(request, 'website/blog_details.html')

def contact(request):
    return render(request, 'website/contact.html')


