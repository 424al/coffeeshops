from __future__ import absolute_import, unicode_literals
from django.shortcuts import render
from django.views.generic import CreateView, View, DetailView, UpdateView, ListView
from django.urls import reverse_lazy
from .models import StoreFront
from .api.serializers import *
from rest_framework import generics
from .forms.new_shop_form import ShopSubmission
import json


# HOME PAGE
def homepage(request):
    # locations = StoreFront.objects.all()
    # json = json.dumps(list(locations))
    # args = {
    #     'locations':json,
    # }
    data = StoreFront.objects.values('name', 'latitude', 'longitude', 'street_address', 'slug')
    json_data = json.dumps(list(data))
    args = {
        'data': json_data,
    }

    return render(request, 'index.html', args)


# CREATE VIEW TO HANDLE NEW LOCATIONS
class AddLocation(CreateView):
    login_url = reverse_lazy("login")

    form_class = ShopSubmission
    model = StoreFront
    template_name = 'shop_registration.html'
    success_url = reverse_lazy('homepage')

    def form_valid(self, form):
        """
        ONLY USE FUNCTION BELOW WHEN TRYING TO
        USE 'created_by' FUNCTIONS OR SIMILAR
        """
        # self.object = form.save(commit=False)
        # self.object.created_by = self.request.user
        # self.object.save()

        return super().form_valid(form)

    def get_form(self, form_class=None):
        form = super(AddLocation, self).get_form(form_class)

        return form


# DETAIL VIEW OF LOCATION
class LocationDetailView(DetailView):
    """
    Class used to view the profile
    of a specific location
    """
    model = StoreFront
    slug_field = "slug"
    slug_url_kwarg = "slug"
    template_name = 'profile/location_profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['location'] = StoreFront.objects.all()
        return context


class ShopListCreate(generics.ListCreateAPIView):
    queryset = StoreFront.objects.all()
    serializer_class = ShopSerializer
