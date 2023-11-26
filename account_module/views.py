
from django.contrib.auth import login, logout
from django.http import Http404, HttpRequest, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.utils.crypto import get_random_string
from account_module.forms import RegisterForm, LoginForm, ForgotPasswordForm, ResetPasswordForm
from food_module.models import User
import json
from .utils.email_service import send_email
import time
# from utils.email_service import send_email


class RegisterView(View):
    def get(self, request):
        login_form = LoginForm()
        register_form = RegisterForm()
        context = {
            'register_form': register_form,
            'login_form': login_form
        }

        return render(request, 'login_register.html', context)

    def post(self, request):

        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        u_pass = body['user_pass']
        u_email = body['user_email']

        u_username = body['user_username']


        if u_username and u_email :
            user: bool = User.objects.filter(email__iexact=u_email ,username__iexact=u_username).exists()
            username: bool = User.objects.filter(username__iexact=u_username).exists()

            if user or username:
                return JsonResponse({
                    'status':'exists',
                    'message':'email or username is exists!'

                })
            else:
                new_user = User(
                    email=u_email,
                    email_active_code=get_random_string(72),
                    is_active=False,
                    username=u_username)
                new_user.set_password(u_pass)
                new_user.save()

                time.sleep(.3)


                send_email(subject='active account',to=new_user.email, context={'user':new_user},template_name='activate_account.html')
                return JsonResponse({
                    'status': 'ok',
                    'message':'check your email for active account'
                })

        login_form = LoginForm()
        register_form = RegisterForm()
        context = {
            'register_form': register_form,
            'login_form': login_form
        }

        return render(request, 'account_module/register.html', context)




def login_req( request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    u_pass = body['user_pass']
    u_email = body['user_email']

    if u_pass and u_email:

       userr= User.objects.filter(email__exact=u_email).first()

       if userr is not None:
         if not userr.is_active:
             return JsonResponse({
                   'status': 'no_active',
                   'message': 'user is not active please check your email!'

               })
         elif not userr.check_password(u_pass):
             return JsonResponse({
                 'status': 'no pass',
                 'message': 'password is not coorect'

             })



         else:
              login(request, userr)
              return JsonResponse({
                  'status': 'ok',


              })

    return redirect('home_page')




class ActivateAccountView(View):
    def get(self, request, email_active_code):


        user: User = User.objects.filter(email_active_code__iexact=email_active_code).first()
        if user :
            if not user.is_active:
                user.is_active=True
                user.email_active_code =get_random_string(72)
                user.save()
                return redirect(reverse('home_page'))
            else:
                return redirect(reverse('home_page'))








class ForgetPasswordView(View):
    def get(self, request: HttpRequest):
        forget_pass_form = ForgotPasswordForm()
        context = {'forget_pass_form': forget_pass_form}
        return render(request, 'forget_password.html', context)

    def post(self, request: HttpRequest):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        u_email = body['user_email']



        if u_email :

            user: User = User.objects.filter(email__iexact=u_email).first()
            if user is not None:
                send_email(' reset password', user.email, {'user': user}, 'email_forgot_pass.html')
                return JsonResponse({
                    'status':'ok',
                    'message':'reset password link send to your email'

                })

        return JsonResponse({
            'status': 'no',
            'message': 'email can not find or it is not active!'
        })





class ResetPasswordView(View):
    def get(self, request: HttpRequest, active_code):
        user: User = User.objects.filter(email_active_code__iexact=active_code).first()
        if user is None:
            return redirect(reverse('login_page'))

        reset_pass_form = ResetPasswordForm()

        context = {
            'reset_pass_form': reset_pass_form,
            'user': user
        }
        return render(request, 'account_module/reset_password.html', context)

    def post(self, request: HttpRequest, active_code):
        reset_pass_form = ResetPasswordForm(request.POST)
        user: User = User.objects.filter(email_active_code__iexact=active_code).first()
        if reset_pass_form.is_valid():
            if user is None:
                return redirect(reverse('login_page'))
            user_new_pass = reset_pass_form.cleaned_data.get('password')
            user.set_password(user_new_pass)
            user.email_active_code = get_random_string(72)
            user.is_active = True
            user.save()
            return redirect(reverse('login_page'))

        context = {
            'reset_pass_form': reset_pass_form,
            'user': user
        }

        return render(request, 'account_module/reset_password.html', context)


def log_out(request):
    logout(request)
    return redirect('login_register')





class dsahboard(View):

    def get(self):
        pass

    def post(self):
        pass




