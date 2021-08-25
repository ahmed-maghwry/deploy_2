from django import forms
from ads.models import  *
# import PIL
order_by_option=(('create_date',"date_up"),('-create_date',"date_down"),('price',"price_up"),('-price',"price_down"),('title',"title_up"),('-title',"title_down"))

class order_by (forms.Form):
    order_by_options = forms.ChoiceField( choices =order_by_option,)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['order_by_options'].widget.attrs.update({'onchange': "this.form.submit()"  })
class order_by_no_ajax (forms.Form):
    order_by_options = forms.ChoiceField( choices =order_by_option,)
    def __init__(self, *args, **kwargs):    
        super().__init__(*args, **kwargs)
        self.fields['order_by_options'].widget.attrs.update({'onchange': "this.form.submit();"  })

class general(forms.ModelForm):
    class Meta:
        model = ads
        fields = [  'sub','end' , 'last'  ]
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['last'].widget.attrs.update({'multiple': 'multiple'})

class price_form (forms.Form):
    from_price = forms.DecimalField(max_digits=14 , decimal_places=4 , label ='price from')
    to_price = forms.DecimalField(max_digits=14 , decimal_places=4 ,  label ='price to')

class car_search(forms.ModelForm):
    class Meta:
        model = db_car
        exclude = ['ad_id' , 'price' ]
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['color'].widget.attrs.update({'multiple': 'multiple'})
        self.fields['body_type'].widget.attrs.update({'multiple': 'multiple'})
        self.fields['year'].widget.attrs.update({'multiple': 'multiple'})
        self.fields['condition'].widget.attrs.update({'multiple': 'multiple'})
        self.fields['payment_option'].widget.attrs.update({'multiple': 'multiple'})
        self.fields['engine_capacity'].widget.attrs.update({'multiple': 'multiple'})
        self.fields['Kilometers'].widget.attrs.update({'multiple': 'multiple'})
        self.fields['transmission_type'].widget.attrs.update({'multiple': 'multiple'})
        








class motorcycles_search(forms.ModelForm):
    class Meta:
        model = db_motorcycles
        exclude = ['ad_id' , 'price' ]

class car_spare_parts_search(forms.ModelForm):
    class Meta:
        model = db_car_spare_parts
        exclude = ['ad_id' , 'price' ]

class Boats_search(forms.ModelForm):
    class Meta:
        model = db_Boats
        exclude = ['ad_id' , 'price' ]

class heavy_trucks_search(forms.ModelForm):
    class Meta:
        model = db_heavy_trucks
        exclude = ['ad_id' , 'price' ]

class mobile_phones_search(forms.ModelForm):
    class Meta:
        model = db_mobile_phones
        exclude = ['ad_id' , 'price' ]

class mobile_accessories_search(forms.ModelForm):
    class Meta:
        model = db_mobile_accessories
        exclude = ['ad_id' , 'price' ]



class properties_search(forms.ModelForm):
    class Meta:
        model = db_properties
        exclude = ['ad_id' , 'price' ]

class properties_ecommer_search(forms.ModelForm):
    class Meta:
        model = db_properties_ecommer
        exclude = ['ad_id' , 'price' ]

class properties_buildings_lands_search(forms.ModelForm):
    class Meta:
        model = db_properties_buildings_lands
        exclude = ['ad_id' , 'price' ]
class furnisher_search(forms.ModelForm):
    class Meta:
        model = db_furnisher
        exclude = ['ad_id' , 'price' ]
class jops_services_search(forms.ModelForm):
    class Meta:
        model = db_jops_services
        exclude = ['ad_id' , 'price' ]
class pets_search(forms.ModelForm):
    class Meta:
        model = db_pets
        exclude = ['ad_id' , 'price' ]
class general_search(forms.ModelForm):
    class Meta:
        model = db_general
        exclude = ['ad_id' , 'price' ]


