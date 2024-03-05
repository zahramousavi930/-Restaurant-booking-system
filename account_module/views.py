import json
import time
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.http import HttpRequest, JsonResponse,HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.crypto import get_random_string
from django.views import View
from django.views.generic import TemplateView
from django.views.generic.edit import UpdateView

from account_module.forms import RegisterForm, LoginForm, ForgotPasswordForm, ResetPasswordForm
from food_module.models import User, reservation, Food_menu, Footer_data
from .models import Order, OrderDetail
from .utils.email_service import send_email



class RegisterView(View):

    def get(self, request):
        footer = Footer_data.objects.all()
        login_form = LoginForm()
        register_form = RegisterForm()
        context = {'register_form': register_form, 'login_form': login_form, 'footer': footer}

        return render(request, 'login_register.html', context)

    def post(self, request):

        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        u_pass = body['user_pass']
        u_email = body['user_email']

        u_username = body['user_username']

        if u_username and u_email:
            user: bool = User.objects.filter(email__iexact=u_email, username__iexact=u_username).exists()
            username: bool = User.objects.filter(username__iexact=u_username).exists()

            if user or username:
                return JsonResponse({'status': 'exists', 'message': 'email or username is exists!'

                                     })
            else:
                new_user = User(email=u_email,
                                email_active_code=get_random_string(72),

                                is_active=False,

                                username=u_username)
                new_user.set_password(u_pass)
                new_user.save()

                time.sleep(.3)

                send_email(subject='active account', to=new_user.email, context={'user': new_user},
                           template_name='activate_account.html')
                return JsonResponse({'status': 'ok', 'message': 'check your email for active account'})

        login_form = LoginForm()
        register_form = RegisterForm()
        context = {'register_form': register_form, 'login_form': login_form}

        return render(request, 'login_register.html', context)


def login_req(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    u_pass = body['user_pass']
    u_email_username = body['user_email']

    check_user_email=User.objects.filter(email=u_email_username).first()
    check_user_username=User.objects.filter(username=u_email_username).first()

    if check_user_email :
        if not check_user_email.is_active:
            return JsonResponse({'status': 'no_active', 'message': 'user is not active please check your email!'})

        elif not check_user_email.check_password(u_pass):
            return JsonResponse({'status': 'no pass', 'message': 'password is not correct'})

        else:
            login(request, check_user_email)
            return JsonResponse({'status': 'ok'})

    if  check_user_username:
        if not check_user_username.is_active:
            return JsonResponse({'status': 'no_active', 'message': 'user is not active please check your email!'})

        elif not check_user_username.check_password(u_pass):
            return JsonResponse({'status': 'no pass', 'message': 'password is not correct'})

        else:
            login(request, check_user_username)
            return JsonResponse({'status': 'ok'})


    return JsonResponse({
        'status': 'data_not_correct',
        'message':'user with this data is not exist'
    })





class ActivateAccountView(View):
    def get(self, request, email_active_code):
        user: User = User.objects.filter(email_active_code__iexact=email_active_code).first()
        if user:
            if not user.is_active:
                user.is_active = True
                user.email_active_code = get_random_string(72)
                user.save()
                return redirect(reverse('home_page'))
            else:
                return redirect(reverse('home_page'))
        else:
            return redirect(reverse('home_page'))



class ForgetPasswordView(View):
    def get(self, request: HttpRequest):
        forget_pass_form = ForgotPasswordForm()
        footer = Footer_data.objects.all()
        context = {'forget_pass_form': forget_pass_form, 'footer': footer}
        return render(request, 'forget_password.html', context)

    def post(self, request: HttpRequest):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        u_email = body['user_email']

        if u_email:

            user: User = User.objects.filter(email__iexact=u_email).first()
            if user is not None:
                send_email(' reset password', user.email, {'user': user}, 'email_forget_pass.html')
                return JsonResponse({'status': 'ok', 'message': 'reset password link send to your email'

                                     })

        return JsonResponse({'status': 'no', 'message': 'email can not find or it is not active!'})


class ResetPasswordView(View):
    def get(self, request: HttpRequest, active_code):

        user: User = User.objects.filter(email_active_code__iexact=active_code).first()
        if user is None:
            return redirect(reverse('login_register'))

        reset_pass_form = ResetPasswordForm()
        footer = Footer_data.objects.all()
        context = {'reset_pass_form': reset_pass_form, 'user': user, 'footer': footer}
        return render(request, 'reset_password.html', context)

    def post(self, request: HttpRequest, active_code):
        reset_pass_form = ResetPasswordForm(request.POST)
        user: User = User.objects.filter(email_active_code__iexact=active_code).first()
        if reset_pass_form.is_valid():
            if user is None:
                return redirect(reverse('login_register'))
            user_new_pass = reset_pass_form.cleaned_data.get('password')

            user.set_password(user_new_pass)
            user.email_active_code = get_random_string(72)
            user.is_active = True
            user.save()
            return redirect(reverse('login_register'))

        context = {'reset_pass_form': reset_pass_form, 'user': user}

        return render(request, 'reset_password.html', context)


def log_out(request):
    logout(request)
    return redirect('login_register')


class edit_dsahboard(UpdateView):
    template_name = 'edit_user_dashboard.html'
    model = reservation
    fields = ['name', 'phone', 'email', 'number_of_guests', 'date', 'timee']
    success_url = '/dashboard/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['footer'] = Footer_data.objects.all()
        return context

    def form_invalid(self, form):
        messages.error(self.request, 'Please check the fields. They are not correct.')
        return super().form_invalid(form)

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:

            return redirect('home_page')
        return super().dispatch(request, *args, **kwargs)



class dsahboard(TemplateView):
    template_name = 'user_dashboard.html'

    def get_context_data(self, **kwargs):
        context = super(dsahboard, self).get_context_data()
        context['footer'] = Footer_data.objects.all()
        context['reserv'] = reservation.objects.filter(add_user=self.request.user).all()
        return context

    def post(self, request):
        if request.GET.get('remove'):
            return JsonResponse({'status': 'remove'})
        else:
            pass


    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:

            return redirect('login_register')
        return super().dispatch(request, *args, **kwargs)





class shoping_cart(TemplateView):
    template_name = 'shoping_cart.html'

    def get_context_data(self, **kwargs):
        current_order, created = Order.objects.get_or_create(is_paid=False, user_id=self.request.user.id)
        total_amount = 0
        for order_detail in current_order.orderdetail_set.all():
            total_amount += order_detail.food.price * order_detail.count

        context = super(shoping_cart, self).get_context_data()
        context['order'] = current_order
        context['sum'] = total_amount
        context['footer'] = Footer_data.objects.all()

        return context
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login_register')
        return super().dispatch(request, *args, **kwargs)


def add_product_to_order(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    pk = body['pk']
    print(pk)


    if request.user.is_authenticated:
        food_order = Food_menu.objects.filter(id=pk, is_active=True).first()
        if food_order is not None:
            current_order, created = Order.objects.get_or_create(is_paid=False, user_id=request.user.id)
            current_order_detail = current_order.orderdetail_set.filter(food_id=pk).first()
            if current_order_detail is not None:
                current_order_detail.count += 1
                current_order_detail.save()
            else:
                new_detail = OrderDetail(order_id=current_order.id, food_id=pk, count=1)
                new_detail.save()

            return JsonResponse({'status': 'success', 'message': ' order add to cart',

                                 })
        else:
            return JsonResponse({'status': 'not_found', 'message': 'food dose not exists',

                                 })
    else:
        return JsonResponse({'status': 'not_auth', 'message': 'please login then order!',})


def remove_reserve(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    pk = body['pk']

    try:
        reserv = reservation.objects.filter(id=pk).delete()
        return JsonResponse({
            'status': 'ok'

                             })
    except:
        return JsonResponse({
            'status':'failed',
            'message':'cant\'t remove reserve'
        })


def modify_order_detail(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    pk = body['pk']

    try:
        m = OrderDetail.objects.filter(food_id=pk, order__user_id=request.user.id)
        m.delete()
        return JsonResponse({'status': 'ok'})

    except:
        pass








def increase_count(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    pk = body['food_pk']

    order_detail = OrderDetail.objects.filter(food_id=pk, order__user_id=request.user.id).first()
    if order_detail:

        order_detail.count += 1
        order_detail.save()
        return JsonResponse({'status': 'ok'})

    return JsonResponse({
        'status':'error'
    })







def decrease_count(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    pk = body['food_pk']


    order_detail = OrderDetail.objects.filter(food_id=pk, order__user_id=request.user.id).first()

    if order_detail:
        if order_detail.count > 1:
            order_detail.count -= 1
            order_detail.save()
            return JsonResponse({'status': 'ok'})
        else:
            order_detail.delete()
            return JsonResponse({'status': 'ok'})
    else:

        return JsonResponse({'status': 'not_found'})