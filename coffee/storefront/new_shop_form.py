from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, HTML, Row, Column, Div, Reset, Field, Submit
from .models import StoreFront
from django.utils.text import format_lazy
from django.utils.translation import ugettext_lazy as _
from parsley.decorators import parsleyfy


@parsleyfy
class ShopSubmission(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super(ShopSubmission,self).__init__(*args,**kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "POST"
        self.helper.form_id = "shop_form"
        self.helper.attrs = {"data-parsley-validate": ""}
        self.helper.layout = Layout(
            Row(
                Column('name', css_class='form-group col-md-3 mb-3'),
                Column('street_address', css_class='form-group col-md-3 mb-3'),
                Column('additional_address_field', css_class='form-group col-md-3 mb-3'),
                # Submit(
                #     'submit', "Submit"
                # )
            ),
            Row(
                Column('city', css_class='form-group col-md-3 mb-3'),
                Column('state', css_class='form-group col-md-3 mb-3'),
                Column('zip_code', css_class='form-group col-md-3 mb-3'),
            ),
            Row(
                Column('latitude', css_class='form-group col-md-3 mb-3'),
                Column('longitude', css_class='form-group col-md-3 mb-3'),
                Column('zip_code', css_class='form-group col-md-3 mb-3'),
            ),
            Row(
                Column('phone', css_class='form-group col-md-3 mb-3'),
                Column('instagram_username', css_class='form-group col-md-3 mb-3'),
            ),
            Submit(
                'submit', "Submit"
            )


        )

    def form_valid(self,form):

        return self.form_invalid(form)

    class Meta:

        model = StoreFront

        fields = {
            'name',
            'street_address',
            'additional_address_field',
            'city',
            'state',
            'zip_code',
            'latitude',
            'longitude',
            'phone',
            'instagram_username'
        }

        labels = {
            'name':_("Store Name"),
            'street_address':_("Address"),
            'additional_address_field':_("Address 2"),
            'city':_("City"),
             'state':_("State"),
             'zip_code':_("Zip Code"),
             'latitude':_("latitude"),
            'longitude':_("longitude"),
             'phone':_("Phone Number"),
             'instagram_username':_("Instagram Username")
        }

        widgets = {
            'name': forms.TextInput(
                attrs={"class": "form-control", "cols": 80, "rows":1}

            ),
            'street_address': forms.TextInput(
                attrs={"class": "form-control", "cols": 80, "rows": 1}

            ),
            'additional_address_field': forms.TextInput(
                attrs={"class": "form-control", "cols": 80, "rows": 1}

            ),
            'city': forms.TextInput(
                attrs={"class": "form-control", "cols": 80, "rows": 1}

            ),
            'state': forms.TextInput(
                attrs={"class": "form-control", "cols": 80, "rows": 1}

            ),
            'zip_code': forms.TextInput(
                attrs={"class": "form-control", "cols": 80, "rows": 1}

            ),
            'latitude': forms.TextInput(
                attrs={"class": "form-control", "cols": 80, "rows": 1}

            ),
            'longitude': forms.TextInput(
                attrs={"class": "form-control", "cols": 80, "rows": 1}

            ),
            'phone': forms.TextInput(
                attrs={"class": "form-control", "cols": 80, "rows": 1}

            ),
            'instagram_username': forms.TextInput(
                attrs={"class": "form-control", "cols": 80, "rows": 1}

            ),
        }