from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User

def login(request):
    # POST 요청이 들어오면 로그인 처리를 해줘야 하고
    if request.method == 'POST':
        userid = request.POST['username']
        pwd = request.POST['password']
        user = auth.authenticate(request, username = userid, password = pwd) 
        # 이 authenticate 메소드는 사용자가 입력한 내용이 실제로 데이터베이스에 있는 내용인지 아닌지 확인해준다.
        # 이미 저장되어있는 회원이라면, User 객체를 반환하고, 그렇지 않다면 None을 반환한다.
        # 장고에는 User 객체가 내장되어 있다.

        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html')


    else:
        return render(request, 'login.html')
    # GET 요청이 들어오면 login form을 담고있는 login.html을 띄워주는 역할을 해야한다.

def logout(request):
    auth.logout(request)
    return redirect('home')