from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from django.views.generic.base import TemplateView

from kilogram.forms import CreateUserForm, UploadForm


class IndexView(ListView):
    context_object_name = 'user_photo_list'
    paginate_by = 2

    def get_queryset(self):
        user = self.request.user
        return user.photo_set.all().order_by('-pub_date')


class CreateUserView(CreateView): # generic view중에 CreateView를 상속받는다.
    template_name = 'registration/signup.html' # 템플릿은?
    form_class =  CreateUserForm # 푸슨 폼 사용? >> 내장 회원가입 폼을 커스터마지징 한 것을 사용하는 경우
    # form_class = UserCreationForm >> 내장 회원가입 폼 사용하는 경우
    success_url = reverse_lazy('create') # 성공하면 어디로?


class RegisteredView(TemplateView): # generic view중에 TemplateView를 상속받는다.
    template_name = 'registration/signup_done.html' # 템플릿은?


@login_required
def upload(request):
    if request.method == "POST":
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.owner = request.user
            form.save()
            return redirect('kilogram:index')
    else:
        form = UploadForm()
    return render(request, 'kilogram/upload.html', {'form': form})