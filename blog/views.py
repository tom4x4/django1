from django.shortcuts import render

from django.views.generic import ListView
from django.utils import timezone
from .models import Person
from .models import Post


class PersonListView(ListView):
    model = Person
    template_name = 'blog/people.html'


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})


