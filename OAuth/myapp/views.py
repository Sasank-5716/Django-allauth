from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def dashboard_view(request):
    return render(request, 'main.html')
