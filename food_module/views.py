from django.views.generic import TemplateView
from . import models
from .forms import Reservation ,comment_form
import json
from django.http import JsonResponse ,HttpResponseRedirect
from django.shortcuts import get_object_or_404 ,reverse

class Home_page(TemplateView):
    template_name ='home.html'

    def get_context_data(self, **kwargs):
        liked =False
        context=super(Home_page, self).get_context_data()
        context['foods']=models.Food_menu.objects.filter(is_active=True)
        context['main_comments']=models.Comments.objects.filter(is_aactive=True)
        context['comment'] = comment_form()


        return context




def comments(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    u_name = body['name']
    u_email = body['email']
    u_text= body['text']

    try:
        new_comments = models.Comments(
            name=u_name,
            email=u_email,
            text_area=u_text,
            is_aactive=False,
        )
        new_comments.save()
        return JsonResponse({
        'status': 'ok',
        'message': 'after checking your comments it will be shown'
        })


    except:
        return JsonResponse({
            'status': 'no',
            'message': 'there is a problem to save comments'
        })


def reserv(request):



    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    u_name= body['name']
    u_phone = body['phone']
    u_email = body['email']
    u_number = body['how_many']
    u_date = body['date']
    u_time = body['time']

    if request.user.is_authenticated:
        set_date= models.reservation(
            name=u_name,
            phone=u_phone,
            email=u_email,
            number_of_guests=u_number,
            date=u_date,
            timee=u_time

        )

        set_date.save()



        return JsonResponse({
            'status': 'ok',
            'message':' reserve was successfully'
        })
    else:
        return JsonResponse({
            'status': 'no',
            'message': 'please login or register first'
        })



def like_part(request,pk):

    if request.user.is_authenticated:
        post=get_object_or_404(models.Food_menu ,id=pk)
        liked=False
        if post.like.filter(id=request.user.id).exists():
            post.like.remove(request.user)
            liked=False
        else:
            post.like.add(request.user)
            liked=True


        return HttpResponseRedirect(reverse('home_page'))
    else:
        return JsonResponse({
            'status': 'no',
            'message':'please login first '
        })









