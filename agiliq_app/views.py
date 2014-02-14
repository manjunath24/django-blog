from django.shortcuts import render, get_object_or_404

from .models import Article, Comment
from .forms import CommentForm

# Create your views here.


def detail(request, slug=None):

    """ Displays detail page with comments
    """
    article = get_object_or_404(Article, slug=slug)
    comments = Comment.objects.filter(blog=article.id, status=1)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.blog = articles
            comment.save()
            form = CommentForm()
            return render(request, 'detail.html', {'article': article,
                                                   'form': form,
                                                   'added': 'success',
                                                   'comments': comments})
    else:
        form = CommentForm()
    return render(request, 'detail.html', {'article': article, 'form': form,
                                           'comments': comments})
