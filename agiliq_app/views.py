from django.shortcuts import render
from agiliq_app.models import Article, Comment
from agiliq_app.forms import CommentForm
# Create your views here.


def detail(request, blog_id=None):

    """ Displays detail page with comments
    """
    data = Article.objects.get(pk=blog_id)
    get_comments = Comment.objects.filter(blog=blog_id, status=1)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            name = request.POST['name']
            email = request.POST['email']
            description = request.POST['description']
            comment = Comment(blog=data, name=name, email=email,
                              dessription=description, status=0)
            comment.save()
            form = CommentForm()
            return render(request, 'detail.html', {'data': data, 'form': form,
                                                   'added': 'success',
                                                   'comments': get_comments})
    else:
        form = CommentForm()
    return render(request, 'detail.html', {'data': data, 'form': form,
                                           'comments': get_comments})
