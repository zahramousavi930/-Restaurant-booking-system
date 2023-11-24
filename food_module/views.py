from django.views.generic import TemplateView
from . import models
from .forms import Reservation
import json
from django.http import JsonResponse ,HttpResponseRedirect
from django.shortcuts import get_object_or_404

class Home_page(TemplateView):
    template_name ='home.html'

    def get_context_data(self, **kwargs):
        context=super(Home_page, self).get_context_data()
        context['foods']=models.Food_menu.objects.filter(is_active=True)
        context['reserve'] = Reservation()
        return context





class Home_page(TemplateView):
    template_name ='home.html'

    def get_context_data(self, **kwargs):

        context=super(Home_page, self).get_context_data()
        context['foods']=models.Food_menu.objects.filter(is_active=True)

        context['reserve'] = Reservation()
        return context




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




