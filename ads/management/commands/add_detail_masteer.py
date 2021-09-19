import datetime
import random
from django.core.management.base import BaseCommand
import random
from ads.models import *

# payment_options=['Cash','Exchange','Installments','Rent']
# payment_options_pets=['Cash','Exchange','Installments','Adoption']

# years=['2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020']
# colors=['Red','White','Silver','Black','Dark Blue','Dark Gray','Dark Green','Light Brown','Gold','Bright Red']
# body_types=['SUV','Sedan','Cabriolet','coupe','Hatchback','Pickup','Bus','Other']
# engine_capacities=['0 - 800','1000 - 1300','1400 - 1600','1800 - 2000','2200 - 2800','More Than 3000']
# Kilometers_list=['0 - 999','1000 - 29999','30000 - 49999','50000 - 99999','100000 - 149999','150000 - 199999','More Than 200000']

# transmission_types=['Automatic','Manual']
# rent_duration=['Daily','Monthly','Yearly']
# rent_options=['With Driver','Without Driver','Both Options']
# condition=['New','Used']
# ad_type=['For Sale','Wanted item']
# warranty=['yes','no']
# yes_or_no=['yes','no']
# sale_rent=['Sale','rent']
# from_one=['1','2','3','4','5','6','7','8','9','10','+11']
# gender_list=(('1',"male"),('2',"female"))
# employment_type_list=['Full-time','Part-time','Internship','Freelance']
# education_level=['Student','High-Secondary School','Diploma','Bachelors Degree','Masters Degree','PhD Degree']
# boolean_list=['0','1']
# names=['Harry Mackay','Virginia	Kerr','Vanessa Bailey','Sam	Mackenzie','Isaac	Smith','Julian	Berry','Kevin	MacDonald','Alexander'	'Alsop','Nicholas'	'Mackay','Joseph'	'Baker','William'	'Parsons','Victoria'	'Watson','Sebastian'	'Mackenzie','Julian'	'Murray','Felicity'	'Metcalfe','Brandon'	'Kerr','Joshua	Dickens','Jessica	Hardacre','Amy'	'Russell','Anna'	'Nash','Donna'	'Newman','Joseph'	'McDonald','Bella'	'Baker','Jasmine'	'Watson','Jonathan'	'Dowd','Matt'	'Lewis','Samantha'	'Abraham','John'	'Nolan','Pippa'	'Parr','Edward'	'Buckland','Emma'	'Grant','Andrew'	'Hughes','Benjamin'	'Dickens','Connor'	'North','Austin'	'Smith','John'	'Hudson','Trevor'	'Turner','Piers'	'Campbell','Alexander'	'Jones','Adam'	'Marshall','Amanda	Kerr','Claire	Gray','Emily	Howard','Carol	Wilkins','Keith	Watson','Jasmine	Ogden','Tim	Pullman','Peter	Randall','Sally	Forsyth','Tim	Slater','Blake	Mackenzie','Phil	Slater','Peter	Fisher','Sebastian	Grant','Jason	Edmunds','Peter	Ince','Cameron	Metcalfe','Kylie	Ball','Oliver	Peters','Eric	Coleman','Olivia	McLean','Brian	Stewart','Karen	Butler','Steven	Hart','Madeleine	Hughes','Joshua	Mitchell','Katherine	Hamilton','Thomas	Hunter','Carolyn	Lewis','Julia	Ross','Sonia	Hardacre','Adam	Knox','Victor	Forsyth','Chloe	Mathis','Kimberly	Coleman','Joseph	Peters','Sue	Walsh','Rachel	Newman','Leonard	Walsh','Heather	Chapman','Peter	Skinner','Christopher	Skinner','Tim	Ball','Carl	Mills','Alexander	Payne','Pippa	Morgan','Sam	Scott','Ella	Slater','Richard	Howard','Alison	Skinner','Joseph Davies','Max	Glover','Vanessa	Rutherford','Thomas	Bell','Adam	Walker','Jack	Lee','Michael	Carr','Jake	Reid','Diana Roberts','William	Glover']




payment_options=['1','2','3','4']
payment_options_pets=['1','2','3','4']

years=['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17']
colors=['1','2','3','4','5','6','7','8','9','10']
body_types=['1','2','3','4','5','6']
engine_capacities=['1','2','3','4','5','6']
Kilometers_list=['1','2','3','4','5','6','7']

transmission_types=['1','2']
rent_duration=['1','2','3']
rent_options=['1','2','3']
condition=['1','2']
ad_type=['1','2']
warranty=['1','2']
yes_or_no=['1','2']
sale_rent=['1','2']
from_one=['1','2','3','4','5','6','7','8','9','10','+11']
employment_type_list=['1','2','3','4']
education_level=['1','2','3','4','5','6']
boolean_list=['0','1']
names=['Harry Mackay','Virginia	Kerr','Vanessa Bailey','Sam	Mackenzie','Isaac	Smith','Julian	Berry','Kevin	MacDonald','Alexander'	'Alsop','Nicholas'	'Mackay','Joseph'	'Baker','William'	'Parsons','Victoria'	'Watson','Sebastian'	'Mackenzie','Julian'	'Murray','Felicity'	'Metcalfe','Brandon'	'Kerr','Joshua	Dickens','Jessica	Hardacre','Amy'	'Russell','Anna'	'Nash','Donna'	'Newman','Joseph'	'McDonald','Bella'	'Baker','Jasmine'	'Watson','Jonathan'	'Dowd','Matt'	'Lewis','Samantha'	'Abraham','John'	'Nolan','Pippa'	'Parr','Edward'	'Buckland','Emma'	'Grant','Andrew'	'Hughes','Benjamin'	'Dickens','Connor'	'North','Austin'	'Smith','John'	'Hudson','Trevor'	'Turner','Piers'	'Campbell','Alexander'	'Jones','Adam'	'Marshall','Amanda	Kerr','Claire	Gray','Emily	Howard','Carol	Wilkins','Keith	Watson','Jasmine	Ogden','Tim	Pullman','Peter	Randall','Sally	Forsyth','Tim	Slater','Blake	Mackenzie','Phil	Slater','Peter	Fisher','Sebastian	Grant','Jason	Edmunds','Peter	Ince','Cameron	Metcalfe','Kylie	Ball','Oliver	Peters','Eric	Coleman','Olivia	McLean','Brian	Stewart','Karen	Butler','Steven	Hart','Madeleine	Hughes','Joshua	Mitchell','Katherine	Hamilton','Thomas	Hunter','Carolyn	Lewis','Julia	Ross','Sonia	Hardacre','Adam	Knox','Victor	Forsyth','Chloe	Mathis','Kimberly	Coleman','Joseph	Peters','Sue	Walsh','Rachel	Newman','Leonard	Walsh','Heather	Chapman','Peter	Skinner','Christopher	Skinner','Tim	Ball','Carl	Mills','Alexander	Payne','Pippa	Morgan','Sam	Scott','Ella	Slater','Richard	Howard','Alison	Skinner','Joseph Davies','Max	Glover','Vanessa	Rutherford','Thomas	Bell','Adam	Walker','Jack	Lee','Michael	Carr','Jake	Reid','Diana Roberts','William	Glover']




main_list=[43,50,53,111,113,114,115,116,117,118,]
_43_list=[44,45,46,47,48,49] #car
_50_list=[51,52] #Mobile Phones & Accessories
_53_list=[54,55,56,57,223,224,225,226,227,228,229,230,231,232,233,234,235] #Electronic Devices
_111_list=[204,205,206,207,208,209,210,211,212]#Properties
_113_list=[236,237,238,239,240,241,242,243,244,245]#Appliances
_114_list=[213,214,215,216,217,218,219,220,221,222,261,262,263,264,265,266,267
,268,269,270,271,272,273,274,275,276,277,278,279,280,281,282,283]#Services
_115_list=[287,288,289,290,291,292,293,294,295,296,297]#Sports & Hobbies
_116_list=[246,247,248,249,250]#Pets - Accessories
_117_list=[194,195,196,197,198,199,200,201,202,203]#Home Furniture
_118_list=[251,252,253,254,255,256]#Babies & Kids
options =["ex", "Sale","free"]
data_ba={
        '44': db_car , '45' : db_car_rent , '46' : db_motorcycles, '47' : db_car_spare_parts,
        '49': db_Boats , '48' : db_heavy_trucks,
        '51': db_mobile_phones,
        '52': db_mobile_accessories ,
        '205' : db_properties,'204' : db_properties ,'212' : db_properties ,'210' : db_properties ,'211' : db_properties ,'207' : db_properties  ,'208' : db_properties_ecommer  ,'209' : db_properties_ecommer  ,'206' : db_properties_buildings_lands ,
        "213" : db_jops_services  ,"214" : db_jops_services ,"215" : db_jops_services ,"216" : db_jops_services ,"217" : db_jops_services ,"218" : db_jops_services ,"219" : db_jops_services ,"220" : db_jops_services ,"221" : db_jops_services ,"222" : db_jops_services ,"261" : db_jops_services ,"262" : db_jops_services ,"263" : db_jops_services ,"264" : db_jops_services ,"265" : db_jops_services ,"266" : db_jops_services ,"267" : db_jops_services ,"268" : db_jops_services ,"269" : db_jops_services ,"270" : db_jops_services ,"271" : db_jops_services ,"272" : db_jops_services ,"273" : db_jops_services ,"274" : db_jops_services ,"275" : db_jops_services ,"276" : db_jops_services ,"277" : db_jops_services ,"278" : db_jops_services ,"279" : db_jops_services ,"280" : db_jops_services ,"281" : db_jops_services ,"282" : db_jops_services ,"283" : db_jops_services ,"284" : db_jops_services ,"285" : db_jops_services ,"286" : db_jops_services  ,
        "203" : db_furnisher ,"194" : db_furnisher ,"199" : db_furnisher ,"200" : db_furnisher ,"201" : db_furnisher ,"198" : db_furnisher ,"197" : db_furnisher ,"202" : db_furnisher ,"196" : db_furnisher ,"195" : db_furnisher ,
        "246" : db_pets ,"247" : db_pets ,"248" : db_pets ,"249" : db_pets ,"250" : db_pets ,
        "54" : db_general,"55" : db_general,"56" : db_general,"57" : db_general,"223" : db_general,"224" : db_general,"225" : db_general,"226" : db_general,"227" : db_general,"228" : db_general,"229" : db_general,"230" : db_general,"231" : db_general,"232" : db_general,"233" : db_general,"234" : db_general,"235" : db_general,"236" : db_general,"237" : db_general,"238" : db_general,"239" : db_general,"240" : db_general,"241" : db_general,"242" : db_general,"243" : db_general,"244" : db_general,"245" : db_general,
        "287" : db_general,"288" : db_general,"289" : db_general,"290" : db_general,"291" : db_general,"292" : db_general,"293" : db_general,"294" : db_general,"295" : db_general,"296" : db_general,"297" : db_general,"251" : db_general,"252" : db_general,"253" : db_general,"254" : db_general,"255" : db_general,"256" : db_general,
    }
class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        for p in range (500000 , 1000000) :

            main=catugry.objects.get(id=random.choice(main_list))

            if main.id==43 :
                sub=catugry.objects.get(id=random.choice(_43_list))
                end=catugry.objects.none()
                if sub.id == 44 :
                    end=random.choice(catugry.objects.filter( main_id=main , sub_id=44, end__isnull=True ))
                else:pass
            elif main.id == 50 :
                sub=catugry.objects.get(id=random.choice(_50_list))
            elif main.id == 53 :
                sub=catugry.objects.get(id=random.choice(_53_list))
            elif main.id == 111 :
                sub=catugry.objects.get(id=random.choice(_111_list))
            elif main.id == 113 :
                sub=catugry.objects.get(id=random.choice(_113_list))
            elif main.id == 114 :
                sub=catugry.objects.get(id=random.choice(_114_list))
            elif main.id == 115 :
                sub=catugry.objects.get(id=random.choice(_115_list))
            elif main.id == 116 :
                sub=catugry.objects.get(id=random.choice(_116_list))
            elif main.id == 117 :
                sub=catugry.objects.get(id=random.choice(_117_list))
            elif main.id == 118 :
                sub=catugry.objects.get(id=random.choice(_118_list))
            else: print(main.id)
            try:
                cat = ads.objects.create(
                title= 'test from command' + str(p),
                description='test from command'+ str(main) + " // " + str(sub),
                main=main,
                sub=sub,
                end=end,
                user_id=1,
                ad_option=random.choice(options),
                name_of_who=random.choice(names))
            except:
                cat = ads.objects.create(
                title= 'test from command' + str(p),
                description='test from command'+ str(main) + " // " + str(sub),
                main=main,
                sub=sub,
                user_id=1,
                ad_option=random.choice(options),
                name_of_who=random.choice(names))
            saved_ad=cat
            details_data=data_ba[str(saved_ad.sub.id)]
            if saved_ad.sub.id == 44 or saved_ad.sub.id == 45 :
                try:
                    detail_ad=details_data.objects.create(ad_id=saved_ad
                    ,payment_option=random.choice(payment_options)
                    ,price = float(random.randrange(1000,10000000))
                    ,ad_type=random.choice(ad_type)
                    ,condition=random.choice(condition)
                    ,year=random.choice(years)
                    ,color=random.choice(colors)
                    ,body_type=random.choice(body_types)
                    ,engine_capacity=random.choice(engine_capacities)
                    ,Kilometers=random.choice(Kilometers_list)
                    ,transmission_type=random.choice(transmission_types)
                    ,abs = random.choice(boolean_list)
                    ,air_conditioning = random.choice(boolean_list)
                    ,airbags = random.choice(boolean_list)
                    ,alarm_System = random.choice(boolean_list)
                    ,radio = random.choice(boolean_list)
                    ,aux_qudio_in = random.choice(boolean_list)
                    ,bluetooth_system = random.choice(boolean_list)
                    ,cruise_control = random.choice(boolean_list)
                    ,edb = random.choice(boolean_list)
                    ,fog_lights = random.choice(boolean_list)
                    ,keyless_start = random.choice(boolean_list)
                    ,leather_seats = random.choice(boolean_list)
                    ,navigation_system = random.choice(boolean_list)
                    ,off_Road_tyres = random.choice(boolean_list)
                    ,parkings_ensors = random.choice(boolean_list)
                    ,power_locks = random.choice(boolean_list)
                    ,power_mirrors = random.choice(boolean_list)
                    ,power_seats = random.choice(boolean_list)
                    ,power_steering = random.choice(boolean_list)
                    ,power_windows = random.choice(boolean_list)
                    ,premium_wheels_rims = random.choice(boolean_list)
                    ,rear_view_camera = random.choice(boolean_list)
                    ,roof_rack = random.choice(boolean_list)
                    ,sunroof = random.choice(boolean_list)
                    ,touch_screen = random.choice(boolean_list)
                    ,usb_charger =random.choice(boolean_list) )
                except:
                    detail_ad=details_data.objects.create(ad_id=saved_ad
                    ,price = float(random.randrange(1000,10000000))
                    ,ad_type=random.choice(ad_type)
                    ,condition=random.choice(condition)
                    ,year=random.choice(years)
                    ,color=random.choice(colors)
                    ,body_type=random.choice(body_types)
                    ,engine_capacity=random.choice(engine_capacities)
                    ,transmission_type=random.choice(transmission_types)
                    ,abs = random.choice(boolean_list)
                    ,air_conditioning = random.choice(boolean_list)
                    ,airbags = random.choice(boolean_list)
                    ,alarm_System = random.choice(boolean_list)
                    ,radio = random.choice(boolean_list)
                    ,aux_qudio_in = random.choice(boolean_list)
                    ,bluetooth_system = random.choice(boolean_list)
                    ,cruise_control = random.choice(boolean_list)
                    ,edb = random.choice(boolean_list)
                    ,fog_lights = random.choice(boolean_list)
                    ,keyless_start = random.choice(boolean_list)
                    ,leather_seats = random.choice(boolean_list)
                    ,navigation_system = random.choice(boolean_list)
                    ,off_Road_tyres = random.choice(boolean_list)
                    ,parkings_ensors = random.choice(boolean_list)
                    ,power_locks = random.choice(boolean_list)
                    ,power_mirrors = random.choice(boolean_list)
                    ,power_seats = random.choice(boolean_list)
                    ,power_steering = random.choice(boolean_list)
                    ,power_windows = random.choice(boolean_list)
                    ,premium_wheels_rims = random.choice(boolean_list)
                    ,rear_view_camera = random.choice(boolean_list)
                    ,roof_rack = random.choice(boolean_list)
                    ,sunroof = random.choice(boolean_list)
                    ,touch_screen = random.choice(boolean_list)
                    ,usb_charger =random.choice(boolean_list) )
            elif saved_ad.sub.id in _50_list :
                detail_ad=details_data.objects.create(ad_id=saved_ad
                ,payment_option=random.choice(payment_options)
                ,price = float(random.randrange(1000,10000000))
                ,ad_type=random.choice(ad_type)
                ,warranty=random.choice(warranty)
                ,condition=random.choice(condition)
                ,color=random.choice(colors))
            elif details_data == db_general :
                detail_ad=details_data.objects.create(ad_id=saved_ad,
                payment_option=random.choice(payment_options),
                price = float(random.randrange(200,10000000)),
                condition=random.choice(condition),
                ad_type=random.choice(ad_type)
                )

            elif saved_ad.sub.id in _111_list :
                detail_ad=details_data.objects.create(ad_id=saved_ad)
            elif saved_ad.sub.id in _113_list :
                detail_ad=details_data.objects.create(ad_id=saved_ad)
            elif saved_ad.sub.id in _114_list :
                detail_ad=details_data.objects.create(ad_id=saved_ad)
            elif saved_ad.sub.id in _115_list :
                detail_ad=details_data.objects.create(ad_id=saved_ad)
            elif saved_ad.sub.id in _116_list :
                detail_ad=details_data.objects.create(ad_id=saved_ad)
            elif saved_ad.sub.id in _117_list :
                detail_ad=details_data.objects.create(ad_id=saved_ad)
            elif saved_ad.sub.id in _118_list :
                detail_ad=details_data.objects.create(ad_id=saved_ad)
            else:detail_ad=details_data.objects.create(ad_id=saved_ad)
            self.stdout.write(self.style.SUCCESS('Data imported successfully'+ str(p)  ))

