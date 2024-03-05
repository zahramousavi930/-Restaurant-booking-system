import json

from django.contrib.auth import get_user_model
from django.test import TestCase, RequestFactory
from django.urls import reverse

from . import models
from .forms import comment_form
from .views import comments

User = get_user_model()


class TestForms(TestCase):

    def test_required_comment(self):
        form = comment_form(data={'c_name': '', 'c_email': '', 'c_text': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('c_name', form.errors.keys())
        self.assertIn('c_email', form.errors.keys())
        self.assertIn('c_text', form.errors.keys())
        self.assertEqual(form.errors['c_name'][0], 'This field is required.')
        self.assertEqual(form.errors['c_email'][0], 'This field is required.')
        self.assertEqual(form.errors['c_text'][0], 'This field is required.')


class test_views(TestCase):

    def test_home_page_view(self):
        response = self.client.get(reverse('home_page'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')
        self.assertIn('foods', response.context)
        self.assertIn('main_comments', response.context)
        self.assertIn('footer', response.context)
        self.assertIn('reserv', response.context)
        self.assertIn('comment', response.context)
        self.assertIsInstance(response.context['comment'], comment_form)


class CommentsTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_valid_comments(self):
        request_data = {'name': 'John Doe', 'email': 'john@example.com', 'text': 'This is a valid comment.'}
        request = self.factory.post(reverse('add_comments'), data=json.dumps(request_data),
                                    content_type='application/json')

        response = comments(request)

        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.content.decode('utf-8'))
        self.assertEqual(response_data['status'], 'ok')
        self.assertEqual(response_data['message'], 'after checking your comments it will be shown')

        saved_comment = models.Comments.objects.filter(name=request_data['name'], email=request_data['email'],
                                                       text_area=request_data['text']).first()
        self.assertIsNotNone(saved_comment)
        self.assertFalse(saved_comment.is_active_comment)

    def test_empty_fields(self):
        request_data = {'name': '', 'email': '', 'text': ''}
        request = self.factory.post(reverse('add_comments'), data=json.dumps(request_data),
                                    content_type='application/json')

        response = comments(request)

        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.content.decode('utf-8'))
        self.assertEqual(response_data['status'], 'no')
        self.assertEqual(response_data['message'], 'name, email, and text cannot be empty')

        saved_comment = models.Comments.objects.filter(email=request_data['email']).first()
        self.assertIsNone(saved_comment)


class ClassificationFoodTestCase(TestCase):
    def test_classification_food_creation(self):
        classification_food = models.Classification_food.objects.create(title='Test Classification')

        saved_classification_food = models.Classification_food.objects.get(title='Test Classification')

        self.assertEqual(saved_classification_food.title, 'Test Classification')


class FoodMenuTestCase(TestCase):
    def setUp(self):
        self.classification = models.Classification_food.objects.create(title='Test Classification')

    def test_food_menu_creation(self):
        food_menu = models.Food_menu.objects.create(food_name='Test Food', slug='test-food',
            about_food='Description of the test food', image='', price=10, Classification=self.classification,
            discount=5)

        saved_food_menu = models.Food_menu.objects.get(food_name='Test Food')

        self.assertEqual(saved_food_menu.food_name, 'Test Food')
        self.assertEqual(saved_food_menu.slug, 'test-food')
        self.assertEqual(saved_food_menu.about_food, 'Description of the test food')
        self.assertEqual(saved_food_menu.price, 10)
        self.assertEqual(saved_food_menu.Classification, self.classification)
        self.assertEqual(saved_food_menu.discount, 5)


class FooterDataTestCase(TestCase):
    def test_footer_data_creation(self):
        footer_data = models.Footer_data.objects.create(phone_number='1234567890', email='example@example.com',
            description='Test description for footer', facebook_link='https://www.facebook.com/example',
            x_link='https://www.example.com/x', linkdin_link='https://www.linkedin.com/example',
            instagram_link='https://www.instagram.com/example', pinterest_link='https://www.pinterest.com/example')

        saved_footer_data = models.Footer_data.objects.get(phone_number='1234567890')

        self.assertEqual(saved_footer_data.phone_number, '1234567890')
        self.assertEqual(saved_footer_data.email, 'example@example.com')
        self.assertEqual(saved_footer_data.description, 'Test description for footer')
        self.assertEqual(saved_footer_data.facebook_link, 'https://www.facebook.com/example')
        self.assertEqual(saved_footer_data.x_link, 'https://www.example.com/x')
        self.assertEqual(saved_footer_data.linkdin_link, 'https://www.linkedin.com/example')
        self.assertEqual(saved_footer_data.instagram_link, 'https://www.instagram.com/example')
        self.assertEqual(saved_footer_data.pinterest_link, 'https://www.pinterest.com/example')


class ReservationTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='testpassword')

    def test_reservation_creation(self):
        reservation_instance = models.reservation.objects.create(name='John Doe', phone='1234567890',
            email='john@example.com', number_of_guests=3, date='2024-03-04', timee='12:00:00')

        reservation_instance.add_user.add(self.user)

        saved_reservation = models.reservation.objects.get(name='John Doe')

        self.assertEqual(saved_reservation.name, 'John Doe')
        self.assertEqual(saved_reservation.phone, '1234567890')
        self.assertEqual(saved_reservation.email, 'john@example.com')
        self.assertEqual(saved_reservation.number_of_guests, 3)
        self.assertEqual(saved_reservation.date.strftime('%Y-%m-%d'), '2024-03-04')
        self.assertEqual(saved_reservation.timee.strftime('%H:%M:%S'), '12:00:00')
        self.assertIn(self.user, saved_reservation.add_user.all())


class CommentsTestCase(TestCase):
    def test_comments_creation(self):
        comment = models.Comments.objects.create(name='John Doe', email='john@example.com',
            text_area='This is a test comment', is_active_comment=False)

        saved_comment = models.Comments.objects.get(name='John Doe')

        self.assertEqual(saved_comment.name, 'John Doe')
        self.assertEqual(saved_comment.email, 'john@example.com')
        self.assertEqual(saved_comment.text_area, 'This is a test comment')
        self.assertFalse(saved_comment.is_active_comment)

        self.assertIsNotNone(saved_comment.date_time)


class CustomUserTestCase(TestCase):
    def test_user_creation(self):
        user = User.objects.create_user(username='testuser', email='test@example.com', password='testpassword',
            email_active_code='activation_code123')

        saved_user = User.objects.get(username='testuser')

        self.assertEqual(saved_user.username, 'testuser')
        self.assertEqual(saved_user.email, 'test@example.com')
        self.assertEqual(saved_user.email_active_code, 'activation_code123')



class ModelTestCase(TestCase):
    def setUp(self):

        self.Classification_food = models.Classification_food.objects.create(title='Test Title')

        self.Footer_data = models.Footer_data.objects.create(phone_number='Test Title')

        self.Comments = models.Comments.objects.create(name='Test Title')

    def test_str_method(self):

        expected_str = 'Test Title'
        self.assertEqual(str(self.Classification_food), expected_str)

        self.assertEqual(str(self.Footer_data), expected_str)
        self.assertEqual(str(self.Comments), expected_str)