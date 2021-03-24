from django.shortcuts import render, redirect, get_object_or_404 # pk값을 이용해 특정 모델 객체 하나만 갖고오는 방법
from .models import Blog
from django.utils import timezone
from .forms import BlogForm, BlogModelForm, CommentForm


def home(request):
    # 블로그 글들을 모조리 띄우는 코드를 여기다 작성해야함
    
    # posts = Blog.objects.all()#위에서 임포트해온 블로그라고 하는 객체들을 모조리 가져오는 코드
    posts = Blog.objects.filter().order_by('date')# 필터를 통해 가져오는 방법 

    return render(request, 'index.html', {'posts': posts})

# 블로그 글 작성 html을 보여주는 함수
def new(request):
    return render(request, 'new.html')

# 블로그 글을 저장해주는 함수
def create(request):
    if(request.method == 'POST'):
        post = Blog()
        post.title = request.POST['title']
        post.body = request.POST['body']
        post.date = timezone.now()
        post.save()
    return redirect('home')

## ** html form 을 이용해서 데이터베이스한테 데이터를 저장하는 방법! ** ##
# new 라고 함수는 new.html이라는 띄어주는 함수인데, form을 띄어주는 함수이다.
# 그 new.html이 띄워진 상태에서 글 생성하기 버튼을 누르면.
# url 'create' 로 POST 요청이 보내질텐데,

# 이 url 'create'가 어떤녀석이냐면 
# 만약에 나(create함수)한테 들어온 그 요청이 POST 요청이라면,
# Blog() 객체를 생성해서, title안에는 request.POST['title'] 를 담고,
# body 안에는 post.body = request.POST['body'] 담고,
# date 안에는 timezone.now() # 현재시간
# 그대로 데이터베이스에 저장해주는  post.save()
# 저장이 끝났다면, 'home'으로 redirect해주는 함수이다.


# Django는 GET요청과 POST요청 모두를 하나의 url에서 처리할 수 있다.
# django form을 이용해서 입력값을 받는 함수
# GET (= 입력값을 받을 수 있는 html을 갖다 줘야함)
# POST (= 입력한 내용을 데이터베이스에 저장 . form에서 입력한 내용을 처리)
def formcreate(request):
    # 입력을 받을 수 있는 html을 갖다주기
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid(): #입력값의 유효성 검사를 위해 .is_vaild() 메서드를 사용한다.
            post = Blog()
            post.title = form.cleaned_data['title']
            post.body = form.cleaned_data['body']
            post.save()
            return redirect('home')
    else:
        form = BlogForm()
    return render(request, 'form_create.html', {'form':form}) 
    # render()의 세번째 인자로 views.py 내의 데이터를 html에 넘겨줄 수있다. 단, 딕셔너리 자료형으로 넘겨줘야 한다.


def modelformcreate(request):
    if request.method == 'POST' or request.method == 'FILES':
        form = BlogModelForm(request.POST, request.FILES)
        if form.is_valid(): 
            form.save()
            return redirect('home')
    else:
        form = BlogModelForm()
    return render(request, 'form_create.html', {'form':form}) 

def detail(request, blog_id):
    # blog_id 번째 블로그 글을 데이터베이스로부터 갖고와서
    blog_detail = get_object_or_404(Blog, pk=blog_id)
    # blog_id 번째 블로그 글을 detail.html로 띄워주는 코드

    comment_form = CommentForm()


    return render(request, 'detail.html', {'blog_detail':blog_detail, 'comment_form':comment_form})


def create_comment(request, blog_id):
    filled_form = CommentForm(request.POST)

    if filled_form.is_valid():
        finished_form = filled_form.save(commit = False)
        finished_form.post = get_object_or_404(Blog, pk=blog_id)
        finished_form.save()
    
    return redirect('detail', blog_id)

