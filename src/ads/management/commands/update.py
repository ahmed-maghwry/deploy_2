import random
from django.core.management.base import BaseCommand
from ads.models import db_general
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
class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        id=115660
        for ad in range(1,800000) :
            # if db_general.objects.get(id=id).price==None:

            cc=db_general.objects.filter(id=id).update(payment_option=random.choice(payment_options),
                price = float(random.randrange(200,10000000)),
                condition=random.choice(condition),
                ad_type=random.choice(ad_type))
            print("okkkkkkkkkkkkkkkkkkkkk")
            id+=1
            # else :id+=1


            self.stdout.write(self.style.SUCCESS('Data imported successfully'+str(id)))

