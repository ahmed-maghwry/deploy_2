from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone



# Create your models here.
class ads(models.Model):
    options =( 
    ("ex", "ex"), 
    ("Sale", "Sale"), 
    ("free", "free"), 
)
    user = models.ForeignKey(User, blank=True , null=True, on_delete=models.CASCADE)
    title =models.CharField(max_length=80)
    description = models.TextField(max_length=500,default='')
    main=models.ForeignKey ( 'catugry',related_name='ad_main',
                            limit_choices_to={'main__isnull':True ,
                             'sub__isnull':True ,
                             'end__isnull':True }
                               , on_delete=models.CASCADE,blank=True,null=True, verbose_name='Main Category')
    sub=models.ForeignKey ( 'catugry' ,related_name='ad_sub',
                            limit_choices_to={'sub__isnull':True ,
                                'main__isnull':False ,
                                 'end__isnull':True }
                                ,on_delete=models.CASCADE,blank=True,null=True, verbose_name='Under Surface Category')
    end=models.ForeignKey ( 'catugry' , related_name='ad_end',
                                limit_choices_to={'sub__isnull':False ,
                                                  'main__isnull':False ,
                                                  'end__isnull':True }

                                ,on_delete=models.CASCADE,blank=True,null=True, verbose_name='Deep Category')
    last=models.ForeignKey ( 'catugry' , related_name='ad_last',
                                limit_choices_to={'sub__isnull':False ,
                                                  'main__isnull':False ,
                                                  'end__isnull':False}
                                ,on_delete=models.CASCADE,blank=True,null=True, verbose_name='Last Category')
    create_date = models.DateTimeField(default=timezone.now)
    active = models.BooleanField(default=True)
    view =models.IntegerField(default=0)
    ad_option = models.CharField(max_length=4, choices=options , default='ex')
    img=models.ImageField(upload_to='post_img2/' , default="img/defu.png")
    name_of_who=models.CharField(max_length=30 , null=True,blank=True)
    adress=models.CharField(max_length=80 , null=True,blank=True)
    mobile =models.PositiveSmallIntegerField( default='11' , null=True,blank=True,)
    email=models.EmailField(default="ahmed_mag22@yahoo.com" , null=True,blank=True)
  
    def save( self,*args,**kwargs ):
        if  self.sub  :
            self.main= self.sub.main

        if self.end :
            self.main=self.end.sub.main
            self.sub=self.end.sub
        if self.last :
            self.main=self.last.end.sub.main
            self.sub=self.last.end.sub
            self.end=self.last.end


            
        super(ads, self).save(*args,**kwargs)

    class Meta:
        ordering = ['-create_date']
    def __str__(self):
        return str (self.id)
class catugry(models.Model):
    name=models.CharField ( max_length=40 , default='')
    main=models.ForeignKey ( 'self', related_name='re_main' ,
                            limit_choices_to={'main__isnull':True ,
                             'sub__isnull':True ,
                             'end__isnull':True }
                               , on_delete=models.CASCADE,blank=True,null=True)
    sub=models.ForeignKey ( 'self' , related_name='re_sub',
                            limit_choices_to={'sub__isnull':True ,
                                'main__isnull':False ,
                                 'end__isnull':True }
                                ,on_delete=models.CASCADE,blank=True,null=True)
    end=models.ForeignKey ( 'self' , related_name='re_end',
                                limit_choices_to={'sub__isnull':False ,
                                                  'main__isnull':False,
                                                  'end__isnull':True }
                                ,on_delete=models.CASCADE,blank=True,null=True)
    

    def save( self,*args,**kwargs ):
        if  self.sub  :
            self.main= self.sub.main

        if self.end :
            self.main=self.end.sub.main
            self.sub=self.end.sub            
        super(catugry, self).save(*args,**kwargs)

    class Meta:
        verbose_name = "catugry"
        verbose_name_plural = "catugry"

    def __str__(self):

        return str(self.name)


payment_options=(('1',"Cash"),('2',"Exchange"),('3',"Installments") , ('4','Rent'))
payment_options_pets=(('1',"Cash"),('2',"Exchange"),('3',"Installments") , ('4','Adoption'))

years=(('1',"2001"),('2',"2002"),('3',"2003"),('4',"2004"),('5',"2005"),('6',"2006"),('7',"2007"),('8',"2008"),('9',"2009"),
        ('10',"2010"),('11',"2011"),('12',"2012"),('13',"2013"),('14',"2014"),('15',"2015"),('16',"2016"),('17',"2017"),
        ('18',"2018"),('19',"2019"),  ('20',"2020"), )
colors=(('1',"Red"),('2',"White "),('3',"Silver "),('4',"Black "),('5',"Dark Blue"),('6',"Dark Gray"),
        ('7',"Dark Green"),('8',"Light Brown"),('9',"Gold "),('10',"Bright Red"))
body_types=(('1',"SUV"),('2',"Sedan"),('3',"Cabriolet"),
        ('4',"coupe"),('5',"Hatchback"),('6',"Pickup"),('7',"Bus"),('8',"Other") )
engine_capacities=(('1',"0 - 800"),('2',"1000 - 1300 "),('3',"1400 - 1600") ,
        ('4',"1800 - 2000"),('5',"2200 - 2800"),('6',"More Than 3000"), )
Kilometers_list=(('1',"0 - 999"),('2',"1000 - 29999 "),('3',"30000 - 49999") ,
        ('4',"50000 - 99999"),('5',"100000 - 149999"),('5',"150000 - 199999"),('6',"More Than 200000"), )
transmission_types=(('1',"Automatic"),('2',"Manual"))
rent_duration=(('1',"Daily"),('2',"Monthly"),('3',"Yearly"))
rent_options=(('1',"With Driver"),('2',"Without Driver"),('3',"Both Options"))
condition=(('1',"New"),('2',"Used"))
ad_type=(('1',"For Sale"),('2',"Wanted item"))
warranty=(('1',"Yes"),('2',"NO"))
yes_or_no=(('1',"Yes"),('2',"NO"))
sale_rent=(('1',"Sale"),('2',"rent"))
from_one=(('1',"1"),('2',"2"),('3',"3"),('4',"4"),('5',"5"),('6',"6"),('7',"7"),('8',"8"),('9',"9"),('10',"10"),('11',"11"),('12',"+11"))
gender_list=(('1',"male"),('2',"female"))
employment_type_list=(('1',"Full-time"),('2',"Part-time"),('3',"Internship"),('3',"Freelance"))
education_level=(('1',"Student"),('2',"High-Secondary School "),('3',"Diploma") ,
        ('4',"Bachelors Degree"),('5',"Masters Degree"),('5',"PhD Degree") )




class db_car(models.Model):
    
    ad_id= models.ForeignKey(ads , to_field='id' ,on_delete=models.CASCADE,blank=True,null=True)
    payment_option=models.CharField(max_length=1, choices=payment_options ,blank=True,null=True)
    price = models.DecimalField(max_digits=14,decimal_places=4,null=True,blank=True)
    ad_type=models.CharField(max_length=2,choices=ad_type,blank=True,null=True)
    condition=models.CharField(max_length=2,choices=condition,blank=True,null=True)
    year=models.CharField(max_length=2,choices=years,blank=True,null=True)
    color=models.CharField(max_length=2,choices=colors  ,blank=True,null=True)
    body_type=models.CharField(max_length=1,choices=body_types,blank=True,null=True)
    engine_capacity=models.CharField(max_length=1,choices=engine_capacities  ,blank=True,null=True)
    Kilometers=models.CharField(max_length=1, choices=Kilometers_list ,blank=True,null=True)
    transmission_type=models.CharField(max_length=1,choices=transmission_types,blank=True,null=True)
    abs = models.BooleanField(default=False)
    air_conditioning = models.BooleanField(default=False)
    airbags = models.BooleanField(default=False)
    alarm_System = models.BooleanField(default=False)
    radio = models.BooleanField(default=False)
    aux_qudio_in = models.BooleanField(default=False)
    bluetooth_system = models.BooleanField(default=False)
    cruise_control = models.BooleanField(default=False)
    edb = models.BooleanField(default=False)
    fog_lights = models.BooleanField(default=False)
    keyless_start = models.BooleanField(default=False)
    leather_seats = models.BooleanField(default=False)
    navigation_system = models.BooleanField(default=False)
    off_Road_tyres = models.BooleanField(default=False)
    parkings_ensors = models.BooleanField(default=False)
    power_locks = models.BooleanField(default=False)
    power_mirrors = models.BooleanField(default=False)
    power_seats = models.BooleanField(default=False)
    power_steering = models.BooleanField(default=False)
    power_windows = models.BooleanField(default=False)
    premium_wheels_rims = models.BooleanField(default=False)
    rear_view_camera = models.BooleanField(default=False)
    roof_rack = models.BooleanField(default=False)
    sunroof = models.BooleanField(default=False)
    touch_screen = models.BooleanField(default=False)
    usb_charger = models.BooleanField(default=False)

    def __str__(self):
        return str (self.ad_id.title)
class db_car_rent(models.Model):
   

    ad_id= models.ForeignKey(ads , to_field='id' ,on_delete=models.CASCADE,blank=True,null=True)
    rent_duration=models.CharField(max_length=1, choices=rent_duration ,blank=True,null=True)
    price = models.DecimalField(max_digits=14,decimal_places=4,null=True,blank=True)
    condition=models.CharField(max_length=2,choices=condition,blank=True,null=True)
    ad_type=models.CharField(max_length=2,choices=ad_type,blank=True,null=True)

    rent_option=models.CharField(max_length=1, choices=rent_options ,blank=True,null=True)
    year=models.CharField(max_length=2,choices=years ,blank=True,null=True)
    color=models.CharField(max_length=2,choices=colors ,blank=True,null=True)
    body_type=models.CharField(max_length=1,choices=body_types,blank=True,null=True)
    engine_capacity=models.CharField(max_length=1,choices=engine_capacities ,blank=True,null=True)
    transmission_type=models.CharField(max_length=1,choices=transmission_types,blank=True,null=True)
    abs = models.BooleanField(default=False)
    air_conditioning = models.BooleanField(default=False)
    airbags = models.BooleanField(default=False)
    alarm_System = models.BooleanField(default=False)
    radio = models.BooleanField(default=False)
    aux_qudio_in = models.BooleanField(default=False)
    bluetooth_system = models.BooleanField(default=False)
    cruise_control = models.BooleanField(default=False)
    edb = models.BooleanField(default=False)
    fog_lights = models.BooleanField(default=False)
    keyless_start = models.BooleanField(default=False)
    leather_seats = models.BooleanField(default=False)
    navigation_system = models.BooleanField(default=False)
    off_Road_tyres = models.BooleanField(default=False)
    parkings_ensors = models.BooleanField(default=False)
    power_locks = models.BooleanField(default=False)
    power_mirrors = models.BooleanField(default=False)
    power_seats = models.BooleanField(default=False)
    power_steering = models.BooleanField(default=False)
    power_windows = models.BooleanField(default=False)
    premium_wheels_rims = models.BooleanField(default=False)
    rear_view_camera = models.BooleanField(default=False)
    roof_rack = models.BooleanField(default=False)
    sunroof = models.BooleanField(default=False)
    touch_screen = models.BooleanField(default=False)
    usb_charger = models.BooleanField(default=False)

    def __str__(self):
        return str (self.ad_id.title)
class db_motorcycles(models.Model):
    ad_id= models.ForeignKey(ads , to_field='id' ,on_delete=models.CASCADE,blank=True,null=True)
    payment_option=models.CharField(max_length=1, choices=payment_options ,blank=True,null=True)
    price = models.DecimalField(max_digits=14,decimal_places=4,null=True,blank=True)
    ad_type=models.CharField(max_length=2,choices=ad_type,blank=True,null=True)
    condition=models.CharField(max_length=2,choices=condition,blank=True,null=True)
    year=models.CharField(max_length=2,choices=years,blank=True,null=True)
    color=models.CharField(max_length=2,choices=colors  ,blank=True,null=True)
    engine_capacity=models.CharField(max_length=1,choices=engine_capacities  ,blank=True,null=True)
    Kilometers=models.CharField(max_length=1, choices=Kilometers_list ,blank=True,null=True)
    transmission_type=models.CharField(max_length=1,choices=transmission_types,blank=True,null=True)

    def __str__(self):
        return str (self.ad_id.title)
class db_car_spare_parts(models.Model):
    ad_id= models.ForeignKey(ads , to_field='id' ,on_delete=models.CASCADE,blank=True,null=True)
    payment_option=models.CharField(max_length=1, choices=payment_options ,blank=True,null=True)
    price = models.DecimalField(max_digits=14,decimal_places=4,null=True,blank=True)
    ad_type=models.CharField(max_length=2,choices=ad_type,blank=True,null=True)
    condition=models.CharField(max_length=2,choices=condition,blank=True,null=True)

    def __str__(self):
        return str (self.ad_id.title)
class db_Boats(models.Model):
    ad_id= models.ForeignKey(ads , to_field='id' ,on_delete=models.CASCADE,blank=True,null=True)
    payment_option=models.CharField(max_length=1, choices=payment_options ,blank=True,null=True)
    price = models.DecimalField(max_digits=14,decimal_places=4,null=True,blank=True)
    ad_type=models.CharField(max_length=2,choices=ad_type,blank=True,null=True)
    condition=models.CharField(max_length=2,choices=condition,blank=True,null=True)

    def __str__(self):
        return str (self.ad_id.title)
class db_heavy_trucks(models.Model):
    ad_id= models.ForeignKey(ads , to_field='id' ,on_delete=models.CASCADE,blank=True,null=True)
    payment_option=models.CharField(max_length=1, choices=payment_options ,blank=True,null=True)
    price = models.DecimalField(max_digits=14,decimal_places=4,null=True,blank=True)
    ad_type=models.CharField(max_length=2,choices=ad_type,blank=True,null=True)
    condition=models.CharField(max_length=2,choices=condition,blank=True,null=True)
    year=models.CharField(max_length=2,choices=years,blank=True,null=True)
    color=models.CharField(max_length=2,choices=colors  ,blank=True,null=True)
    engine_capacity=models.CharField(max_length=1,choices=engine_capacities  ,blank=True,null=True)
    Kilometers=models.CharField(max_length=1, choices=Kilometers_list ,blank=True,null=True)
    transmission_type=models.CharField(max_length=1,choices=transmission_types,blank=True,null=True)

    def __str__(self):
        return str (self.ad_id.title)
class db_mobile_phones(models.Model):
    ad_id= models.ForeignKey(ads , to_field='id' ,on_delete=models.CASCADE,blank=True,null=True)
    payment_option=models.CharField(max_length=1, choices=payment_options ,blank=True,null=True)
    price = models.DecimalField(max_digits=14,decimal_places=4,null=True,blank=True)
    ad_type=models.CharField(max_length=2,choices=ad_type,blank=True,null=True)
    warranty=models.CharField(max_length=2,choices=warranty,blank=True,null=True)
    condition=models.CharField(max_length=2,choices=condition,blank=True,null=True)
    color=models.CharField(max_length=2,choices=colors  ,blank=True,null=True)

    def __str__(self):
        return str (self.ad_id.title)
class db_mobile_accessories(models.Model):
    ad_id= models.ForeignKey(ads , to_field='id' ,on_delete=models.CASCADE,blank=True,null=True)
    payment_option=models.CharField(max_length=1, choices=payment_options ,blank=True,null=True)
    price = models.DecimalField(max_digits=14,decimal_places=4,null=True,blank=True)
    ad_type=models.CharField(max_length=2,choices=ad_type,blank=True,null=True)
    warranty=models.CharField(max_length=2,choices=warranty,blank=True,null=True)
    condition=models.CharField(max_length=2,choices=condition,blank=True,null=True)
    color=models.CharField(max_length=2,choices=colors  ,blank=True,null=True)

    def __str__(self):
        return str (self.ad_id.title)
class db_properties (models.Model):
    ad_id= models.ForeignKey(ads , to_field='id' ,on_delete=models.CASCADE,blank=True,null=True)
    payment_option=models.CharField(max_length=1, choices=payment_options ,blank=True,null=True)
    price = models.DecimalField(max_digits=14,decimal_places=4,null=True,blank=True)
    ad_type=models.CharField(max_length=1,choices=ad_type,blank=True,null=True)
    for_sale_rent=models.CharField(max_length=1,choices=sale_rent,blank=True,null=True)
    level= models.CharField(max_length=2,choices=from_one,blank=True,null=True)
    bedrooms= models.CharField(max_length=2,choices=from_one,blank=True,null=True)
    bathrooms= models.CharField(max_length=2,choices=from_one,blank=True,null=True)
    area = models.DecimalField(max_digits=8,decimal_places=2,null=True,blank=True , verbose_name='Area (m²) ')
    furnished = models.CharField(max_length=1,choices=yes_or_no,blank=True,null=True)
    Compound = models.CharField(max_length=1,choices=yes_or_no,blank=True,null=True)
    balcony = models.BooleanField(default=False)
    private_Garden = models.BooleanField(default=False)
    central_ac_heating = models.BooleanField(default=False)
    water_Meter = models.BooleanField(default=False)
    natural_Gas = models.BooleanField(default=False)
    electricity_Meter = models.BooleanField(default=False)
    covered_Parking = models.BooleanField(default=False)
    maids_Room = models.BooleanField(default=False)
    security = models.BooleanField(default=False)
    pets_allowed = models.BooleanField(default=False)
    landline = models.BooleanField(default=False)
    elevator = models.BooleanField(default=False)
class db_properties_ecommer(models.Model):
    ad_id= models.ForeignKey(ads , to_field='id' ,on_delete=models.CASCADE,blank=True,null=True)
    payment_option=models.CharField(max_length=1, choices=payment_options ,blank=True,null=True)
    price = models.DecimalField(max_digits=14,decimal_places=4,null=True,blank=True)
    ad_type=models.CharField(max_length=1,choices=ad_type,blank=True,null=True)
    for_sale_rent=models.CharField(max_length=1,choices=sale_rent,blank=True,null=True)
    level= models.CharField(max_length=2,choices=from_one,blank=True,null=True)
    bedrooms= models.CharField(max_length=2,choices=from_one,blank=True,null=True)
    bathrooms= models.CharField(max_length=2,choices=from_one,blank=True,null=True)
    area = models.DecimalField(max_digits=8,decimal_places=2,null=True,blank=True , verbose_name='Area (m²) ')
    furnished = models.CharField(max_length=1,choices=yes_or_no,blank=True,null=True)
    Compound = models.CharField(max_length=1,choices=yes_or_no,blank=True,null=True)
    central_ac_heating = models.BooleanField(default=False)
    water_Meter = models.BooleanField(default=False)
    natural_Gas = models.BooleanField(default=False)
    electricity_Meter = models.BooleanField(default=False)
    covered_Parking = models.BooleanField(default=False)
    security = models.BooleanField(default=False)
    landline = models.BooleanField(default=False)
    elevator = models.BooleanField(default=False)
class db_properties_buildings_lands(models.Model):
    ad_id= models.ForeignKey(ads , to_field='id' ,on_delete=models.CASCADE,blank=True,null=True)
    payment_option=models.CharField(max_length=1, choices=payment_options ,blank=True,null=True)
    price = models.DecimalField(max_digits=14,decimal_places=4,null=True,blank=True)
    ad_type=models.CharField(max_length=1,choices=ad_type,blank=True,null=True)
    for_sale_rent=models.CharField(max_length=1,choices=sale_rent,blank=True,null=True)
    level= models.CharField(max_length=2,choices=from_one,blank=True,null=True)
    bedrooms_in_level= models.CharField(max_length=2,choices=from_one,blank=True,null=True)
    bathrooms_in_level= models.CharField(max_length=2,choices=from_one,blank=True,null=True)
    area = models.DecimalField(max_digits=8,decimal_places=2,null=True,blank=True , verbose_name='Area (m²) ')
    Compound = models.CharField(max_length=1,choices=yes_or_no,blank=True,null=True)
    central_ac_heating = models.BooleanField(default=False)
    water_Meter = models.BooleanField(default=False)
    natural_Gas = models.BooleanField(default=False)
    electricity_Meter = models.BooleanField(default=False)
    covered_Parking = models.BooleanField(default=False)
    security = models.BooleanField(default=False)
    landline = models.BooleanField(default=False)
    elevator = models.BooleanField(default=False)
class db_furnisher(models.Model):

    ad_id= models.ForeignKey(ads , to_field='id' ,on_delete=models.CASCADE,blank=True,null=True)
    payment_option=models.CharField(max_length=1, choices=payment_options ,blank=True,null=True)
    price = models.DecimalField(max_digits=14,decimal_places=4,null=True,blank=True)
    condition=models.CharField(max_length=2,choices=condition,blank=True,null=True)
    ad_type=models.CharField(max_length=1,choices=ad_type,blank=True,null=True)
    room_area = models.DecimalField(max_digits=8,decimal_places=3,null=True,blank=True , verbose_name='Area (m²) ')


class db_pets(models.Model):
    ad_id= models.ForeignKey(ads , to_field='id' ,on_delete=models.CASCADE,blank=True,null=True)
    payment_option=models.CharField(max_length=1, choices=payment_options_pets ,blank=True,null=True)
    price = models.DecimalField(max_digits=14,decimal_places=4,null=True,blank=True)
    gender=models.CharField(max_length=2,choices=gender_list,blank=True,null=True)
    ad_type=models.CharField(max_length=1,choices=ad_type,blank=True,null=True)
    age = models.DecimalField(max_digits=14,decimal_places=4,null=True,blank=True)
class db_jops_services(models.Model):
    ad_id= models.ForeignKey(ads , to_field='id' ,on_delete=models.CASCADE,blank=True,null=True)
    price = models.DecimalField(max_digits=14,decimal_places=4,null=True,blank=True ,verbose_name='Salary' )
    gender=models.CharField(max_length=1,choices=gender_list,blank=True,null=True)
    education=models.CharField(max_length=1,choices=education_level,blank=True,null=True)
    ad_type=models.CharField(max_length=1,choices=ad_type,blank=True,null=True)
    age = models.DecimalField(max_digits=14,decimal_places=4,null=True,blank=True)
    employment_type=models.CharField(max_length=1,choices=employment_type_list,blank=True,null=True)

class db_general(models.Model):
    ad_id= models.ForeignKey(ads , to_field='id' ,on_delete=models.CASCADE,blank=True,null=True)
    payment_option=models.CharField(max_length=1, choices=payment_options ,blank=True,null=True)
    price = models.DecimalField(max_digits=14,decimal_places=4,null=True,blank=True)
    condition=models.CharField(max_length=2,choices=condition,blank=True,null=True)
    ad_type=models.CharField(max_length=1,choices=ad_type,blank=True,null=True)



