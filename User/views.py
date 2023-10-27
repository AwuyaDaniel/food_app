from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, Http404
from .forms import *
from .models import CustomUserManager, CustomUser
from django.views.generic import View
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages



class UserCreateView(View):
    form_class = UserCreationForm
    template_name = 'User/signup.html'

    # blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            # new = form.save(commit=False)
            # new.phone = '+' + new.phone
            # new.save()

            messages.success(request, "Staff has been created successfully")

            return redirect('UserProfile:login')

        return render(request, self.template_name, {'form': form})


class LoginView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('food:index'))
        return render(request, 'User/login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        # print(user)
        if user is not None:
            # print('Yes')
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('food:index'))
            else:
                return render(request, 'User/login.html',
                              {'error_message': 'Your account has been disabled'})
        else:
            # messages.error(request, "Invalid login details")
            return render(request, 'User/login.html', {'error_message': 'Your account does not exist or has been disabled'})


def get_user(request):

    if request.user != request.user:
        raise Http404

    user = request.user

    context = {'user': user, }

    return render(request, 'User/profile.html', context)


def get_users(request):

    if request.user != request.user:
        raise Http404

    data = CustomUser.objects.all().order_by()

    pages = Paginator(data, 6)
    page_number = request.GET.get('page')
    page = pages.get_page(page_number)
    context = {'page': page, 'data': data}

    return render(request, 'User/users.html', context)


def get_single_user(request, email):
    data = CustomUser.objects.get(email=email)
    context = {'user': data}
    return render(request, "User/user_page.html", context)


class LogoutView(View):
    form_class = UserForm
    template_name = '#'

    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse('food:index'))


def deactivate(request):

    if request.user != request.user:
        raise Http404

    user = request.user
    user.is_active = 0
    user.save()

    return HttpResponseRedirect(reverse('food:index'))


# def user_update(request):
#     if request.user != request.user:
#         raise Http404
#
#     user = request.user
#     user_id = UserModel.objects.get(id=user.id)
#
#     form = UserUpdateForm(instance=user_id, data=request.POST)
#     if request.method == 'POST':
#         if form.is_valid():
#             new = form.save(commit=False)
#             new.phone = '+' + new.phone
#             new.save()
#
#             return redirect('userprofile:user_profile')
#
#     context = {'user': user, 'form': form}
#
#     return render(request, 'userprofile/profile.html', context)
#
#
# def change_password(request):
#     if request.user != request.user:
#         raise Http404
#
#     user_loop = UserModel.objects.all()
#     user = request.user
#
#     if request.method == 'POST':
#         user_mod = request.POST.get('id')
#         password1 = request.POST.get('password')
#         password = request.POST.get('password1')
#
#         if password1 == password:
#             user_to_change = UserModel.objects.get(id=int(user_mod))
#             user_to_change.set_password(password)
#             user_to_change.save()
#
#             return redirect('homepage')
#
#     contex = {'user_loop': user_loop, 'user': user}
#
#     return render(request, 'userprofile/password.html', contex)
#
#
# def user_change_password(request):
#     if request.user != request.user:
#         raise Http404
#
#     user = request.user
#
#     if request.method == 'POST':
#         password1 = request.POST.get('password')
#         password = request.POST.get('password1')
#
#         if password1 == password:
#             user_to_change = UserModel.objects.get(id=int(user.id))
#             user_to_change.set_password(password)
#             user_to_change.save()
#
#             return redirect('homepage')
#
#     contex = {'user': user}
#
#     return render(request, 'userprofile/change-password.html', contex)
