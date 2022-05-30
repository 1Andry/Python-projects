from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.views.generic import DetailView, CreateView, FormView, ListView
from django.urls import reverse_lazy
from .models import AddSong
from .forms import UploadFileForm, RegisterUserForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class Base(LoginView):
    template_name = 'player/base.html'


def show_songs(request):
    songs = AddSong.objects.all()
    return render(request, 'player/ss.html', {'songs': songs})


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'player/register.html'
    success_url = reverse_lazy('base')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        return dict(list(context.items()))

    # def form_valid(self, form):
    #     user = form.save
    #     login(self.request, user)
    #     return redirect('base')


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'player/login.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        return dict(list(context.items()))


# def model_form_upload(request):
#     if request.method == 'POST':
#         form = DocumentForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('base')
#     else:
#         form = DocumentForm()
#     return render(request, 'player/upload.html', {
#         'form': form
#     })


def add_song(request):
    if request.method == 'POST':
        song = UploadFileForm(request.POST, request.FILES)
        if song.is_valid():
            song.save()
            return redirect('base')
    else:
        song = UploadFileForm()
    return render(request, 'player/upload.html', {'song': song})

# class UserPage(FormView):
#     form_class = Content
#     template_name = 'player/user_page.html'

# def get_context_data(self, *args, **kwargs):
#     context = super().get_context_data(**kwargs)
#     return dict(list(context.items()))


#
#     def get_context_data(self, *args, **kwargs):
#         context = super().get_context_data(**kwargs)
#         # page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
#         # context['page_user'] = page_user
#         return context
# class ShowProfilePageView(DetailView):
#     model = Profile
#     template_name = 'base/user_profile.html'

# def get_context_data(self, *args, **kwargs):
#     users = Profile.objects.all()
#     context = super(ShowProfilePageView, self).get_context_data(**kwargs)
#     page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
#     context['page_user'] = page_user
#     return context


# def get_queryset(self):
#     return Profile.objects.all()

# def get_context_data(self, *, object_list=None, **kwargs):
#     context = super().get_context_data(**kwargs)
#     # c_def = self.get_user_context(title='Регистрация')
#     context['title'] = 'Регистрация'
#     return context

#

#


#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         # c_def = self.get_user_context(title='Авторизация')
#         context['title'] = 'Авторизация'
#         return context

# class UserPage():
#     page =
# class RegisterUser(CreateView):
#     form_class = RegisterUserForm
#     template_name = 'player/register.html'
#     success_url = reverse_lazy('index')
