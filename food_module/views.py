import json

from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from . import models
from .forms import comment_form ,ReservationForm



class Home_page(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        liked = False
        context = super(Home_page, self).get_context_data()
        context['foods'] = models.Food_menu.objects.filter(is_active=True)
        context['main_comments'] = models.Comments.objects.filter(is_active_comment=True)
        context['footer'] = models.Footer_data.objects.all()
        context['reserv'] = models.reservation.objects.all()
        context['comment'] = comment_form()

        return context



class Book_table(View):
    template_name = 'book2.html'

    def get(self, request, *args, **kwargs):
            form = ReservationForm()
            context = {
                'footer': models.Footer_data.objects.all(),
                'form':form
            }
            return render(request, self.template_name, context)


    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            body_unicode = request.body.decode('utf-8')
            body = json.loads(body_unicode)
            u_name = body['name']
            u_email = body['email']
            u_phone = body['phone']
            u_number = body['how_many']
            u_date = body['date']
            u_time = body['time']

            new_reserve = models.reservation(name=u_name, email=u_email, phone=u_phone, number_of_guests=u_number,
                date=u_date, timee=u_time)
            try:
                new_reserve.save()
                a = models.User.objects.get(id=request.user.id)
                new_reserve.add_user.add(a)
                return JsonResponse({'status': 'ok', 'message': 'reserve set successfully'})

            except:
                return JsonResponse({'status': 'error', 'message': 'data is not correct please check the data'})

        else:
          return JsonResponse({'status': 'no', 'message': 'please login first.'}, status=401)




def comments(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    u_name = body.get('name')
    u_email = body.get('email')
    u_text = body.get('text')

    if not (u_name and u_email and u_text):  # Check if any of the fields are empty
        return JsonResponse({'status': 'no', 'message': 'name, email, and text cannot be empty'})

    try:
        new_comments = models.Comments(name=u_name, email=u_email, text_area=u_text, is_active_comment=False)
        new_comments.save()
        return JsonResponse({'status': 'ok', 'message': 'after checking your comments it will be shown'})
    except Exception as e:
        print(e)
        return JsonResponse({'status': 'error', 'message': 'there is a problem to save comments'})





def like_part(request):
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        pk = body.get('pk')

        if pk:
            if request.user.is_authenticated:
                post = get_object_or_404(models.Food_menu, id=pk)
                liked = False
                if post.like_user.filter(id=request.user.id).exists():
                    post.like_user.remove(request.user)
                    liked = False
                    return JsonResponse({'status': 'disliked'})
                else:
                    post.like_user.add(request.user)
                    liked = True
                    return JsonResponse({'status': 'liked'})
            else:
                return JsonResponse({'status': 'no', 'message': 'Please login first.'})
        else:
            return JsonResponse({'status': 'error1', 'message': 'No post ID provided in request.'})
    else:
        return JsonResponse({'status': 'error2', 'message': 'Only POST requests are allowed.'})



class about_us(TemplateView):
    template_name = 'about_us.html'

    def get_context_data(self, **kwargs):
        context = super(about_us, self).get_context_data()
        context['footer'] = models.Footer_data.objects.all()

        return context
