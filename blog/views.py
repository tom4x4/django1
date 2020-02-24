from django.shortcuts import render
from django.shortcuts import redirect

from django.views.generic import ListView
from django.utils import timezone
from .models import Person
from .models import Post
import time
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from .forms import DocumentForm



class PersonListView(ListView):
    model = Person
    template_name = 'blog/people.html'

def czas():
    czasik=time.time()
    return czasik


def ulogin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        xxx = 'poszlo POST'
        if user is not None:
            login(request, user)
            # Redirect to a success page.
        else:
            # Redirect to a success page.
            xxx='Kiszka'
    else:
        xxx='Kiszka bez POST'
    return render(request, 'blog/login.html', {'zalogowany' : xxx})



#@login_required
def post_list(request):

    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    if request.user.is_authenticated:
       ala=request.user
       edek=User.objects.values_list('password').get(username='edek')
       #edek2=User.objects.filter(username='edek')
       if request.method == "POST":
            #edek=request.META.get('REMOTE_ADDR')
            edek2 = request.POST['guzik']
       else:
           edek2 = 'zzzzzz'

       liczba = 1

    else:
        edek = 'wylogowany'
        edek2 = 'zzzzzz'
        ala="Nie ma kota"
        liczba = 2
    return render(request, 'blog/post_list.html', {'posts': posts, 'czas':czas(),'ala' : ala, 'edek' : edek, 'edek2' : edek2, 'liczba' : liczba})

def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('upload')
    else:
        form = DocumentForm()
    return render(request, 'blog/upload.html', {
        'form': form
    })







