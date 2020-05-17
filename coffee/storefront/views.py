from django.shortcuts import render
from .models import StoreFront

from django.views.generic import CreateView
from .new_shop_form import ShopSubmission
from django.urls import reverse_lazy
import json

# Create your views here.



class Test(CreateView):
    form_class = ShopSubmission
    model = StoreFront
    template_name = 'shop_registration.html'
    success_url = reverse_lazy('mysite')

    def get_form(self, form_class=None):
        form = super(Test,self).get_form(form_class)

        return form




def homepage(request):
    # locations = StoreFront.objects.all()
    # json = json.dumps(list(locations))
    # args = {
    #     'locations':json,
    # }
    data = StoreFront.objects.values('name','latitude','longitude')
    json_data = json.dumps(list(data))
    args = {
            'data': json_data,
            }

    return render(request,'index.html',args)