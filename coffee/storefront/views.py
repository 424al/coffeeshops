from django.shortcuts import render
from .models import StoreFront
from django.views.generic import CreateView
from .new_shop_form import ShopSubmission
from django.urls import reverse_lazy
# Create your views here.
class Test(CreateView):
    form_class = ShopSubmission
    model = StoreFront
    template_name = 'index.html'
    success_url = reverse_lazy('test_form')

    def get_form(self, form_class=None):
        form = super(Test,self).get_form(form_class)

        return form