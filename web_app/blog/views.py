from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'title': "Blog",
        'heading': "Blog",
        "subheading" : "Ini Halaman Blog App"

    }
    return render(request, 'blog/index.html', context)

def singelBlog(request):
    context = {
        'title': "Blog singel",
        'heading': "Blog singel",
        "subheading" : "Ini Halaman Blog App"

    }
    return render(request, 'blog/blog-singel.html', context)
