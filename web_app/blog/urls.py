from django.urls import path


from . import views
import blog

urlpatterns = [
    path('', views.index, name='blog'),
    path('singel-blog/', views.singelBlog, name='singel-blog'),
]