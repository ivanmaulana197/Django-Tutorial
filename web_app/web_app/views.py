from django.shortcuts import render

def index(request):
    context = {
        'title': 'Home',
        'heading': 'Selamat Datang',
        'subheading': 'di kelas Web App Django'
    }
    return render(request, 'index.html',context)


def login(request):
    return render(request, 'login.html')