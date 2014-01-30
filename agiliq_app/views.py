from django.shortcuts import render
from agiliq_app.models import Article,Comment
from agiliq_app.forms import CommentForm
# Create your views here.

def home(request):
	data = Article.objects.all().order_by('-pub_date')
	return render(request,'index.html',{'data':data,'home':True})


def detail(request,blog_id=None):
	
	data = Article.objects.filter(pk=blog_id)
	get_comments = Comment.objects.filter(blogid=blog_id,status=1)

	if request.method == 'POST':
		form = CommentForm(request.POST)
		if form.is_valid():
			name = request.POST['name']
			email = request.POST['email']
			description = request.POST['description']
			comment = Comment(blogid=blog_id,name=name,email=email,dessription=description,status=0)
			comment.save()
			form = CommentForm()
			return render(request,'detail.html',{'data':data,'form':form,'added':'success','comments':get_comments})
	else:
		form = CommentForm()
	return render(request,'detail.html',{'data':data,'form':form,'comments':get_comments})	


def about(request):

	return render(request,'about.html',{'about':True})
