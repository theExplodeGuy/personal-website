from django.shortcuts import render
from .models import Post, Home, Project, Comment
from .forms import CommentForm
from django.views import generic
from django.shortcuts import get_object_or_404



# Create your views here.

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog.html'


class DetailView(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'

def blog_detail(request, slug):
    post = Post.objects.get(slug=slug)
    print(post)
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                post=post
            )
            comment.save()

    try:
        comments = Comment.objects.filter(post=post)
    except Comment.DoesNotExist:
        comments = None

    context = {
        "post": post,
        "comments": comments,
        "form": form,
    }
    return render(request, "post_detail.html", context)

class HomeList(generic.ListView):
    queryset = Home.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'


class HomeDetails(generic.DetailView):
    model = Home
    template_name = 'qualification_detail.html'


class Contact(generic.TemplateView):
    template_name = 'contact_page.html'


def project_index(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'project_index.html', context)

def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {
        'project': project
    }
    return render(request, 'project_detail.html', context)