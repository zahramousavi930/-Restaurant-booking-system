from django.test import TestCase
from .forms import comment_form
# Create your tests here.
from .models import reservation,Comments


class test_forms(TestCase):

    def test_requierd_comment(self):
        form=comment_form({'c_name','','c_email','','c_text',''})
        self.assertFalse(form.is_valid())
        self.assertIn('c_name',form.errors.keys())
        self.assertIn('c_email',form.errors.keys())
        self.assertIn('c_text',form.errors.keys())
        self.assertEqual(form.errors['c_name'][0],'This field is required.')
        self.assertEqual(form.errors['c_email'][0],'This field is required.')
        self.assertEqual(form.errors['c_text'][0],'This field is required.')

    def test_requierd_reservation(self):
        form = reservation({'name', '', 'phone', '', 'email', ''})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())
        self.assertIn('phone', form.errors.keys())
        self.assertIn('email', form.errors.keys())
        self.assertEqual(form.errors['name'][0], 'This field is required.')
        self.assertEqual(form.errors['phone'][0], 'This field is required.')
        self.assertEqual(form.errors['email'][0], 'This field is required.')


class test_views(TestCase):
    def test_reservaion_view(self):
        response=self.client.get('BookTable')
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'book2.html')

    def test_comments_view(self):
        comment=Comments.objects.create(name='Test to add comments')
        response =self.client.get('comment')



    def test_about_us_view(self):
        response = self.client.get('about-us')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about_us.html')







