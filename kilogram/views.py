from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic.base import TemplateView

from kilogram.forms import CreateUserForm


class IndexView(TemplateView): # TemplateView를 상속 받는다.
    template_name = 'kilogram/index.html'


class CreateUserView(CreateView): # generic view중에 CreateView를 상속받는다.
    template_name = 'registration/signup.html' # 템플릿은?
    form_class =  CreateUserForm # 푸슨 폼 사용? >> 내장 회원가입 폼을 커스터마지징 한 것을 사용하는 경우
    # form_class = UserCreationForm >> 내장 회원가입 폼 사용하는 경우
    success_url = reverse_lazy('create') # 성공하면 어디로?


class RegisteredView(TemplateView): # generic view중에 TemplateView를 상속받는다.
    template_name = 'registration/signup_done.html' # 템플릿은?