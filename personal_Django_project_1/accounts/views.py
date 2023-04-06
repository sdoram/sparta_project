# view
"""
장고에서 제공하는 기능을 최대한 사용해 구현해봅시다.
아래 from ... import ... 구문이 힌트입니다. 
지금은 해당 함수가 어떻게 구현되어있는지 전부다 이해 할 수는 없겠지만 
지금까지 공부한 내용으로 이해할 수 있는 부분이 있을겁니다.
모르는 부분이 있다면 지금입니다. 공부할 타이밍!
"""
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import SignupForm
from django.views.decorators.csrf import csrf_exempt


# csrf_token 보안 토큰 무시
@csrf_exempt
def signup(request):
    # 회원 가입 view
    # if request가 POST로 오면
    if request.method == "POST":
        # forms의 SignupForm 사용
        form = SignupForm(request.POST)
        # form의 값이 유효하면
        if form.is_valid():
            form.save()
            return redirect('/sign-in/')
    else:
        form = SignupForm()
    return render(request, 'accounts/signup.html', {'form': form})


def user_login(request):
    # 로그인 view
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        # 유효성 검사
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            # redirect로 변경 해야함
            return render(request, 'erp/main.html')
        else:
            return HttpResponse('로그인 실패')
    else:
        return render(request, 'accounts/signin.html')


@login_required
def user_logout(request):
    # 로그아웃 view
    logout(request)
    return redirect('/')
