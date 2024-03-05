import json

from django.contrib.auth import get_user_model
from django.test import RequestFactory
from django.test import TestCase, Client
from django.urls import reverse , reverse_lazy
from django.utils.crypto import get_random_string

from food_module.models import User, Footer_data, reservation, Food_menu
from .forms import LoginForm, RegisterForm
from .models import Order, OrderDetail
from .views import RegisterView


class DecreaseCountTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='password123')
        self.food = Food_menu.objects.create(food_name='Test Food', price=10)
        self.order = Order.objects.create(user=self.user, is_paid=False)
        self.order_detail = OrderDetail.objects.create(order=self.order, food=self.food, count=2)

    def test_decrease_count_success(self):
        self.client.login(username='testuser', password='password123')
        data = {'food_pk': self.food.pk}
        response = self.client.post(reverse('decrease'), json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['status'], 'ok')

        self.order_detail.refresh_from_db()
        self.assertEqual(self.order_detail.count, 1)

    def test_decrease_count_remove(self):
        self.client.login(username='testuser', password='password123')

        self.order_detail.count = 1
        self.order_detail.save()
        data = {'food_pk': self.food.pk}
        response = self.client.post(reverse('decrease'), json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['status'], 'ok')

        self.assertFalse(OrderDetail.objects.filter(pk=self.order_detail.pk).exists())

    def test_decrease_count_not_found(self):
        self.client.login(username='testuser', password='password123')
        data = {'food_pk': 999}
        response = self.client.post(reverse('decrease'), json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['status'], 'not_found')


class IncreaseCountTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='password123')
        self.food = Food_menu.objects.create(food_name='Test Food', price=10)
        self.order = Order.objects.create(user=self.user, is_paid=False)
        self.order_detail = OrderDetail.objects.create(order=self.order, food=self.food, count=1)

    def test_increase_count_success(self):
        self.client.login(username='testuser', password='password123')
        data = {'food_pk': self.food.pk}
        response = self.client.post(reverse('increase'), json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['status'], 'ok')

        self.order_detail.refresh_from_db()
        self.assertEqual(self.order_detail.count, 2)

    def test_increase_count_failure(self):
        self.client.login(username='testuser', password='password123')
        data = {'food_pk': 999}
        response = self.client.post(reverse('increase'), json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertNotIn('status', 'error')

        self.order_detail.refresh_from_db()
        self.assertEqual(self.order_detail.count, 1)


class ModifyOrderDetailTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='password123')
        self.order = Order.objects.create(user=self.user, is_paid=False)
        self.food = Food_menu.objects.create(food_name='Test Food', price=10)
        self.order_detail = OrderDetail.objects.create(order=self.order, food=self.food, count=1)

    def test_modify_order_detail_success(self):
        self.client.login(username='testuser', password='password123')
        data = {'pk': self.order_detail.food_id}
        response = self.client.post(reverse('modify_order'), json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['status'], 'ok')
        self.assertFalse(OrderDetail.objects.filter(pk=self.order_detail.pk).exists())

    def test_modify_order_detail_failure(self):
        self.client.login(username='testuser', password='password123')
        data = {'pk': 999}
        response = self.client.post(reverse('modify_order'), json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertNotIn('status', 'ok')
        self.assertTrue(OrderDetail.objects.filter(pk=self.order_detail.pk).exists())


class RemoveReservationTestCase(TestCase):
    def setUp(self):
        self.client = Client()

        self.reservation = reservation.objects.create(name='Test Reservation')

    def test_remove_reservation_success(self):
        data = {'pk': self.reservation.pk}
        response = self.client.post(reverse('remove_reserve'), json.dumps(data), content_type='application/json')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['status'], 'ok')

        self.assertFalse(reservation.objects.filter(pk=self.reservation.pk).exists())

    def test_remove_reservation_failure(self):
        data = {'pk': 999}
        response = self.client.post(reverse('remove_reserve'), json.dumps(data), content_type='application/json')

        self.assertEqual(response.status_code, 200)
        self.assertNotIn('status', 'ok')

        self.assertTrue(reservation.objects.filter(pk=self.reservation.pk).exists())


class AddProductToOrderTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='password123')

    def test_add_product_to_order_authenticated(self):
        self.client.login(username='testuser', password='password123')
        food = Food_menu.objects.create(food_name='Test Food', is_active=True)
        data = {'pk': food.pk}
        response = self.client.post(reverse('add_product_to_order'), json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['status'], 'success')
        self.assertEqual(response.json()['message'], ' order add to cart')
        current_order = Order.objects.get(user=self.user, is_paid=False)
        current_order_detail = OrderDetail.objects.get(order=current_order, food=food)
        self.assertEqual(current_order_detail.count, 1)


class RegisterFormTest(TestCase):
    def test_valid_form(self):
        form_data = {'username': 'testuser', 'email': 'test@example.com', 'password': 'testpassword123'}
        form = RegisterForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        form_data = {'email': 'test@example.com', 'password': 'testpassword123'}
        form = RegisterForm(data=form_data)
        self.assertFalse(form.is_valid())
        print(form.errors)
        self.assertIn('username', form.errors)

        form_data['username'] = 'testuser'
        form_data['email'] = 'invalid_email'
        form = RegisterForm(data=form_data)
        self.assertFalse(form.is_valid())
        print(form.errors)
        self.assertIn('email', form.errors)


class LoginFormTest(TestCase):
    def test_valid_form(self):
        form_data = {'email_or_username': 'testuser', 'password': 'testpassword123'}
        form = LoginForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        form_data = {'password': 'testpassword123'}
        form = LoginForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('email_or_username', form.errors)

        form_data['email_or_username'] = 'testuser'
        form_data['password'] = ''
        form = LoginForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('password', form.errors)


class RegisterViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_get(self):
        request = self.factory.get('/register/')
        response = RegisterView.as_view()(request)

        self.assertEqual(response.status_code, 200)

    def test_post_valid_data(self):
        request_data = {'user_pass': 'password123', 'user_email': 'test@example.com', 'user_username': 'testuser'}
        request = self.factory.post('/register/', data=json.dumps(request_data), content_type='application/json')
        response = RegisterView.as_view()(request)

        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.content.decode('utf-8'))

        self.assertIn('ok', response_data['status'])


class LoginTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = get_user_model().objects.create_user(username='testuser', email='test@example.com',
                                                         password='password123', email_active_code='abc123')
        self.user.is_active = True
        self.user.save()

    def test_login_success(self):
        data = {'user_email': 'test@example.com', 'user_pass': 'password123'}

        response = self.client.post('/user/login', json.dumps(data), content_type='application/json')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['status'], 'ok')

    def test_login_inactive_user(self):
        self.user.is_active = False
        self.user.save()

        data = {'user_email': 'test@example.com', 'user_pass': 'password123'}

        response = self.client.post('/user/login', json.dumps(data), content_type='application/json')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['status'], 'no_active')

    def test_login_incorrect_password(self):
        data = {'user_email': 'test@example.com', 'user_pass': 'wrong_password'}

        response = self.client.post('/user/login', json.dumps(data), content_type='application/json')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['status'], 'no pass')

    def test_login_incorrect_username_email(self):
        data = {'user_email': 'nonexistent@example.com', 'user_pass': ''}

        response = self.client.post('/user/login', json.dumps(data), content_type='application/json')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['status'], 'data_not_correct')


class ActivateAccountViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='password123',
                                             email_active_code='abc123')

    def test_activate_account_success(self):
        activation_code = get_random_string(72)
        self.user.email_active_code = activation_code
        self.user.is_active = False
        self.user.save()

        response = self.client.get(reverse('activate_account', args=[activation_code]))

        self.user.refresh_from_db()

        self.assertTrue(self.user.is_active)

        self.assertNotEqual(self.user.email_active_code, activation_code)

        self.assertRedirects(response, reverse('home_page'))

    def test_activate_account_already_activated(self):
        self.user.is_active = True
        self.user.save()

        response = self.client.get(reverse('activate_account', args=['abc123']))

        self.assertTrue(self.user.is_active)

        self.assertRedirects(response, reverse('home_page'))


class ForgetPasswordViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='password123')

    def test_get_forget_password_page(self):
        response = self.client.get(reverse('forget_password_page'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'forget_password.html')

    def test_post_forget_password_invalid_email(self):
        data = {'user_email': 'invalid@example.com'}
        response = self.client.post(reverse('forget_password_page'), json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['status'], 'no')
        self.assertEqual(response.json()['message'], 'email can not find or it is not active!')

    def test_post_forget_password_empty_email(self):
        data = {'user_email': ''}
        response = self.client.post(reverse('forget_password_page'), json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['status'], 'no')
        self.assertEqual(response.json()['message'], 'email can not find or it is not active!')


class ResetPasswordViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser',
         email='test@example.com', 
         password='password123',
          email_active_code='abc123')

    # def test_get_reset_password_page(self):
    #     response = self.client.get(reverse('reset_password_page', kwargs={'active_code': 'abc123'}))
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'reset_password.html')


#     def test_post_reset_password_invalid_code(self):
#         data = {'password': 'new_password', 'confirm_password': 'new_password'}
#         response = self.client.post(reverse('reset_password_page', kwargs={'active_code': 'invalid_code'}), data)
#         self.assertEqual(response.status_code, 302)
#         self.assertRedirects(response, reverse('login_register'))

#     def test_post_reset_password_invalid_form(self):
#         data = {'password': '', 'confirm_password': ''}
#         response = self.client.post(reverse('reset_password_page', kwargs={'active_code': 'abc123'}), data)
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'reset_password.html')

#         self.assertTrue('reset_pass_form' in response.context)
#         form = response.context['reset_pass_form']
#         self.assertFalse(form.is_valid())



class ShoppingCartViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='password123')
        self.footer_data = Footer_data.objects.create()

    def test_get_shopping_cart_page(self):
        self.client.login(username='testuser', password='password123')
        response = self.client.get(reverse_lazy('shoping_cart'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shoping_cart.html')

        self.assertTrue('order' in response.context)
        self.assertTrue('sum' in response.context)
        self.assertTrue('footer' in response.context)
