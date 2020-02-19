from django.shortcuts import render

from django.views.generic import ListView
from django.utils import timezone
from .models import Person
from .models import Post
import time
from django.contrib.auth.models import User



class PersonListView(ListView):
    model = Person
    template_name = 'blog/people.html'

def czas():
    czasik=time.time()
    return czasik

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    if request.user.is_authenticated:
       ala=request.user
       edek=User.objects.values_list('password').get(username='edek')
       #edek2=User.objects.filter(username='edek')
       if request.method == "POST":
            #edek=request.META.get('REMOTE_ADDR')
            edek2 = request.POST.get('guzik')
       else:
           edek2 = 'zzzzzz'

    else:
       ala="Nie ma kota"
    return render(request, 'blog/post_list.html', {'posts': posts, 'czas':czas(),'ala' : ala, 'edek' : edek, 'edek2' : edek2})









