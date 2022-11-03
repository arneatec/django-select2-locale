from django.shortcuts import render
from .models import Post
from django.views.generic import CreateView
from .forms import PostCreateForm
from django.urls import reverse


def index(request):
    context = {
        "posts_count" : Post.objects.count(),
    }
    return render(request, "blog/index.html", context)


class PostCreateView(CreateView):
    model = Post
    form_class = PostCreateForm

    template_name = 'blog/add_post.html'

    def get_success_url(self):
        return reverse("blog_index")
