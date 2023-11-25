from django.shortcuts import render
from django.contrib.auth import login
from django.http import Http404, HttpRequest, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.crypto import get_random_string
from django.views import View
from django.utils.crypto import get_random_string
from account_module.forms import RegisterForm, LoginForm
from food_module.models import User
import json
# Create your views here.




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
        u_confirm_pass = body['user_pass_con']
        u_username = body['user_username']


        if u_username and u_email :
            user: bool = User.objects.filter(email__iexact=u_email).exists()
            if user:
                return JsonResponse({
                    'status':'exists',
                    'message':'email is exists!'

                })
            else:
                new_user = User(
                    email=u_email,
                    email_active_code=get_random_string(72),
                    is_active=False,
                    username=u_username)
                new_user.set_password(u_pass)
                new_user.save()
                # send_email('فعالسازی حساب کاربری', new_user.email, {'user': new_user}, 'emails/activate_account.html')
                return JsonResponse({
                    'status': 'ok',
                    'message':'register successfully'
                })

        login_form = LoginForm()
        register_form = RegisterForm()
        context = {
            'register_form': register_form,
            'login_form': login_form
        }

        return render(request, 'account_module/register.html', context)





