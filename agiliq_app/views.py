from django.shortcuts import render

from .models import Article, Comment
from .forms import CommentForm
# Create your views here.


def detail(request, blog_id=None):

    """ Displays detail page with comments
    """
    articles = Article.objects.get(pk=blog_id)
    get_comments = Comment.objects.filter(blog=blog_id, status=1)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.blog = articles
            comment.save()
            form = CommentForm()
            return render(request, 'detail.html', {'articles': articles,
                                                   'form': form,
                                                   'added': 'success',
                                                   'comments': get_comments})
    else:
        form = CommentForm()
    return render(request, 'detail.html', {'articles': articles, 'form': form,
                                           'comments': get_comments})
