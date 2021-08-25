from django import forms
from . models import *

import PIL
from django.forms.widgets import RadioSelect

class car(forms.ModelForm):
    

    class Meta:
        model = db_car
        exclude = ['ad_id']
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            # self.BooleanField.widget.forms.update(RadioSelect)
            # .widget.attrs.update({'class': 'special'})
            # widget=forms.RadioSelect
            # self.fields['comment'].widget.attrs.update(size='40')

class adsform(forms.ModelForm):
    class Meta:
        model = ads
        fields = [ 'title', 'description' , 'ad_option' , 'main' 
                , 'sub','end' , 'last' , 'img','name_of_who','adress','mobile','email' ]
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


        # self.fields['sub'].queryset = catugry.objects.none()
        # self.fields['end'].queryset = catugry.objects.none()
        # self.fields['last'].queryset = catugry.objects.none()

        # self.fields['last'].widget = forms.HiddenInput()
#         if 'main' in self.data:
#             try:
#                 main_id = int(self.data.get('main'))
#                 self.fields['sub'].queryset = catugry.objects.filter(main_id=main_id , sub_id=None).order_by('name')
#             except (ValueError, TypeError):
#                 pass  # invalid input from the client; ignore and fallback to empty City queryset
#         elif self.instance.pk:
#             pass
#             self.fields['sub'].value = self.instance.main.sub_set.order_by('name')   

#             self.fields['sub'].queryset = self.instance.main.sub_set.order_by('name')   
# #################################################################
#         if 'sub' in self.data:
#             try:
#                 sub_id = int(self.data.get('sub'))
#                 self.fields['end'].queryset = catugry.objects.filter(main_id=main_id ,sub_id=sub_id ,end_id=None).order_by('name')
#             except (ValueError, TypeError):
#                 pass  # invalid input from the client; ignore and fallback to empty City queryset
#         elif self.instance.pk:
#             self.fields['end'].queryset = self.instance.main.sub.end_set.order_by('name')   
# #################################################################
#         if 'end' in self.data:
#             try:
#                 end_id = int(self.data.get('end'))
#                 self.fields['last'].queryset = catugry.objects.filter(main_id=main_id ,sub_id=sub_id ,end_id=end_id ).order_by('name')
#             except (ValueError, TypeError):
#                 pass  # invalid input from the client; ignore and fallback to empty City queryset
#         elif self.instance.pk:
#             self.fields['last'].queryset = self.instance.main.sub.end_set.order_by('name')


        
         
# class adsform2(forms.ModelForm):
#     class Meta:
#         model = ads
#         fields = ['title', 'description' , 'ad_option' , 'main' 
#                 , 'sub','end' , 'last' , 'img','name_of_who','adress','mobile','email' ]
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         if self.instance.main == None or self.instance.sub == None or self.instance.end == None or self.instance.last == None  :
#             self.fields['sub'].queryset = catugry.objects.none()
#             self.fields['end'].queryset = catugry.objects.none()
#             self.fields['last'].queryset = catugry.objects.none()


            
#         else:

#             pass
#         try:
#             if self.instance.main.id :
#                 main_id = self.instance.main.id
#                 self.fields['sub'].queryset = catugry.objects.filter(main_id=main_id , sub_id=None).order_by('name')
#             elif self.instance.sub.id :
#                 sub_id = self.instance.sub.id
#                 self.fields['end'].queryset = catugry.objects.filter(main_id=main_id ,sub_id=sub_id ,end_id=None).order_by('name')

#             elif self.instance.end.id :
#                 end_id = self.instance.end.id
#                 self.fields['last'].queryset = catugry.objects.filter(main_id=main_id ,sub_id=sub_id ,end_id=end_id ).order_by('name')
#             else:
#                 pass
#         except :
#             if 'main' in self.data:
#                 try:
#                     main_id = int(self.data.get('main'))
#                     self.fields['sub'].queryset = catugry.objects.filter(main_id=main_id , sub_id=None).order_by('name')
#                 except (ValueError, TypeError):
#                     pass  # invalid input from the client; ignore and fallback to empty City queryset
#             elif self.instance.pk:
#                 self.fields['sub'].value = self.instance.main.sub_set.order_by('name')   
#     #################################################################
#             if 'sub' in self.data:
#                 try:
#                     sub_id = int(self.data.get('sub'))
#                     self.fields['end'].queryset = catugry.objects.filter(main_id=main_id ,sub_id=sub_id ,end_id=None).order_by('name')
#                 except (ValueError, TypeError):
#                     pass  # invalid input from the client; ignore and fallback to empty City queryset
#             elif self.instance.pk:
#                 self.fields['end'].queryset = self.instance.main.sub.end_set.order_by('name')   
#     #################################################################
#             if 'end' in self.data:
#                 try:
#                     end_id = int(self.data.get('end'))
#                     self.fields['last'].queryset = catugry.objects.filter(main_id=main_id ,sub_id=sub_id ,end_id=end_id ).order_by('name')
#                 except (ValueError, TypeError):
#                     pass  # invalid input from the client; ignore and fallback to empty City queryset
#             elif self.instance.pk:
#                 self.fields['last'].queryset = self.instance.main.sub.end_set.order_by('name')


class motorcycles(forms.ModelForm):
    class Meta:
        model = db_motorcycles
        exclude = ['ad_id'  ]

class car_spare_parts(forms.ModelForm):
    class Meta:
        model = db_car_spare_parts
        exclude = ['ad_id'  ]

class Boats(forms.ModelForm):
    class Meta:
        model = db_Boats
        exclude = ['ad_id' ]

class heavy_trucks(forms.ModelForm):
    class Meta:
        model = db_heavy_trucks
        exclude = ['ad_id' ]

class mobile_phones(forms.ModelForm):
    class Meta:
        model = db_mobile_phones
        exclude = ['ad_id' ]

class mobile_accessories(forms.ModelForm):
    class Meta:
        model = db_mobile_accessories
        exclude = ['ad_id' ]



class properties(forms.ModelForm):
    class Meta:
        model = db_properties
        exclude = ['ad_id' ]

class properties_ecommer(forms.ModelForm):
    class Meta:
        model = db_properties_ecommer
        exclude = ['ad_id' ]

class properties_buildings_lands(forms.ModelForm):
    class Meta:
        model = db_properties_buildings_lands
        exclude = ['ad_id' ]
class furnisher(forms.ModelForm):
    class Meta:
        model = db_furnisher
        exclude = ['ad_id' ]
class jops_services(forms.ModelForm):
    class Meta:
        model = db_jops_services
        exclude = ['ad_id' ]
class pets(forms.ModelForm):
    class Meta:
        model = db_pets
        exclude = ['ad_id' ]
class general(forms.ModelForm):
    class Meta:
        model = db_general
        exclude = ['ad_id' ]
