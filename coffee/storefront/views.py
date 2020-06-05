from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .models import StoreFront
from .new_shop_form import ShopSubmission
import json

# Create your views here.


class Test(LoginRequiredMixin,CreateView):
    login_url = reverse_lazy("login")
    redirect_field_name = None

    form_class = ShopSubmission
    model = StoreFront
    template_name = 'shop_registration.html'
    success_url = reverse_lazy('mysite')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.created_by = self.request.user
        self.object.save()
        return super().form_valid(form)



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