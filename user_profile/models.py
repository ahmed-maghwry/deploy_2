from django.db import models
from django.contrib.auth.models import User
from ads.models import  ads
from allauth import app_settings as allauth_app_settings

# Create your models here.
overnorates_list = (
    ('1',"Beheira"),('2',"Asyut"),('3',"Damietta"),('4',"Kafr El Sheikh"),('5',"Beni Suef"),('6',"New Valley"),('7',"Dakahlia"),('8',"Ismailia"),('9',"Cairo"),('10',"Faiyum"),('11',"North Sinai"),('12',"Luxor"),('13',"Giza"),('14',"Gharbia"),('15',"Port Said"),('16',"Matruh"),('17',"Minya"),('18',"Monufia"),('19',"Qalyubia"),('20',"Qena"),('21',"Red Sea"),('22',"Sharqia"),('23',"Sohag"),('24',"South Sinai"),('25',"Suez"),('26',"Aswan"),('27',"Alexandria"))


class governorate(models.Model):
    name=models.CharField ( max_length=40 , default='')
    governorate_name=models.ForeignKey ( 'self', related_name='re_governorate_name' ,
                            limit_choices_to={'governorate_name__isnull':True ,
                             'center_city__isnull':True ,
                             'region_village__isnull':True }
                               , on_delete=models.CASCADE,blank=True,null=True)
    center_city=models.ForeignKey ( 'self' , related_name='re_center_city',
                            limit_choices_to={'governorate_name__isnull':False ,
                                'center_city__isnull':True ,
                                 'region_village__isnull':True }
                                ,on_delete=models.CASCADE,blank=True,null=True)
    region_village=models.ForeignKey ( 'self' , related_name='re_region_village',
                                limit_choices_to={'governorate_name__isnull':False ,
                                                  'center_city__isnull':False,
                                                  'region_village__isnull':True }
                                ,on_delete=models.CASCADE,blank=True,null=True)
    

    def save( self,*args,**kwargs ):
        if  self.center_city  :
            self.governorate_name= self.center_city.governorate_name

        if self.region_village :
            self.governorate_name=self.region_village.center_city.governorate_name
            self.center_city=self.region_village.center_city            
        super(governorate, self).save(*args,**kwargs)

    class Meta:
        verbose_name = "governorate"
        verbose_name_plural = "governorate"

    def __str__(self):

        return str(self.name)

class adress_details (models.Model):
    user = models.ForeignKey(allauth_app_settings.USER_MODEL,verbose_name=('user'),on_delete=models.CASCADE)
    governorate_name=models.ForeignKey ( 'governorate', related_name='cho_governorate_name' ,
                            limit_choices_to={'governorate_name__isnull':True ,
                             'center_city__isnull':True ,
                             'region_village__isnull':True }
                               , on_delete=models.CASCADE,blank=True,null=True)
    center_city=models.ForeignKey ( 'governorate' , related_name='cho_center_city',
                            limit_choices_to={'governorate_name__isnull':False ,
                                'center_city__isnull':True ,
                                 'region_village__isnull':True }
                                ,on_delete=models.CASCADE,blank=True,null=True)
    region_village=models.ForeignKey ( 'governorate' , related_name='cho_region_village',
                                limit_choices_to={'governorate_name__isnull':False ,
                                                  'center_city__isnull':False,
                                                  'region_village__isnull':True }
                                ,on_delete=models.CASCADE,blank=True,null=True)
    last=models.ForeignKey ( 'governorate' , related_name='cho_last',
                            limit_choices_to={'governorate_name__isnull':False ,
                                                'center_city__isnull':False ,
                                                'region_village__isnull':False}
                            ,on_delete=models.CASCADE,blank=True,null=True, verbose_name='Last adress')
    adress_description = models.CharField(max_length=120)

class user_details (models.Model):
    user = models.ForeignKey(allauth_app_settings.USER_MODEL,verbose_name=('user'),on_delete=models.CASCADE)

    favoret_ads = models.ManyToManyField(ads)
    phone_number = models.PositiveIntegerField(blank=True,null=True) 
    messages_ok = models.BooleanField(default=True)


def __str__(self):

    return str(self.user)
