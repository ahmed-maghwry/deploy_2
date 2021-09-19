
from django.core.management.base import BaseCommand
from user_profile.models import governorate









class Command(BaseCommand):


    def handle(self, *args, **kwargs):

        Home_Appliances =[
            'Alexandria',
            'Aswan',
            'Asyut',
            'Beheira	',
            'Beni Suef',
            'Cairo',
            'Dakahlia',
            'Damietta',
            'Faiyum	',
            'Gharbia	',
            'Giza',
            'Ismailia',
            'Kafr El Sheik',
            'Luxor',
            'Matruh',
            'Minya',
            'Monufia	',
            'New Valley',
            'North Sinai',
            'Port Said',
            'Qalyubia',
            'Qena',
            'Red Sea',
            'Sharqia',
            'Sohag',
            'South Sinai',
            'Suez',

                    ]
        
    

    
        for name1 in Home_Appliances:
            name=name1
            print(name)
            # main=catugry.objects.get(id=115)
            # print(main)

            # main=main
            # sub=sub
            # end=end

            cat = governorate.objects.get_or_create(
                name=name ,
                # main=main
                # sub_id=44
                # end=end
                )

        self.stdout.write(self.style.SUCCESS('Data imported successfully'))

