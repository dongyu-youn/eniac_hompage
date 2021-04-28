from django.shortcuts import render, redirect, reverse
from django.views.generic import FormView
from . import forms
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.contrib.messages.views import SuccessMessageMixin
from open_source import models as Open_Source_models

# Create your views here.

class LoginView(FormView, SuccessMessageMixin):
    template_name = "users/login.html"
    form_class = forms.LoginForm
    success_url = reverse_lazy("core:price")
    initial = {"email": ""}
    success_message = "Profile Updated"

    def form_valid(self, form):
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(self.request, username=email, password=password)
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)
 
def log_out(request):
    logout(request)
    return redirect(reverse("core:price"))

class SignUpView(FormView):
    template_name = "users/signup.html"
    form_class = forms.SignUpForm
    success_url = reverse_lazy("core:price")

    def form_valid(self, form):
        form.save()
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(self.request, username=email, password=password)
        Open_Source_models.OpenSource.objects.create(OpenSource_host=user)
        print(user)

        if user is not None:
            login(self.request, user)
        return super().form_valid(form)
    # initial = {
    #     "first_name": 1,
    #     "last_name": 2,
    #     "email": "11@naver.com"
    # }

    # def form_valid(self, form):
    #     form.save()
    #     email = form.cleaned_data.get("email")
    #     password = form.cleaned_data.get("password")
    #     # 이 유저가 username 과 password가 같다면 그 유저 정보를 가져와줘
    #     # 이러헥 authenticate하는 이유는 password를 회원가입 할 때 저장할때 내가 2로 비밀번호를 설정했다고 가정하면
    #     # django는 이 2를 1ㄹ23ㅁ1ㄴㅇ32ㄹ1ㅁ32ㄴㅇㄹ13ㅁ2ㄴㅇ1ㄹ32ㅁㄴ1ㅇ23ㄹ 암호화 해서 저장을한다.
    #     # models.User.objects.get(username=email, password=password) 이러면 못가져온다 이유는 password가 다르기 때문에 2 가 아니라 1ㄹ23ㅁ.,.,, 암호화 된거기때문에
    #     # 그래서 username과 password로 로그인 하고 싶을 경우는 authenticate를 써야한다!
    #     # 내가 models.User.objects.get(username=email) 만 해서 login(self.request, user) 는 가능하다
    #     # 하지만 우리가 로그인 한다라는 의미는 아이디와 비밀번호를 쳐서 로그인 한다는 개념이기 때문에 authenticate를 쓰는게 로그인 하는 것이다.
    #     user = authenticate(self.request, username=email, password=password)
    #     print(user)
    #     if user is not None:
    #         # 유저를 로그인 시키겠다.
    #         login(self.request, user)
    #         # models.verify_email()
    #     return super().form_valid(form)