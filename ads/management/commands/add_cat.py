from django.core.management.base import BaseCommand
from ads.models import catugry




class Command(BaseCommand):


    def handle(self, *args, **kwargs):

        Home_Appliances =[
            'Sports Equipment' ,
            'Antiques - Collectibles' ,
            'Musical Instruments',
            'Books' ,
            'Other Items' ,
            'Bicycles' ,
            'Movies - Music' ,
            'Study Tools' ,
            'Luggage' ,
            'Board - Card Games' ,
            'Tickets - Vouchers' ,

                    ]
        
    

    
        for name1 in Home_Appliances:
            name=name1
            print(name)
            main=catugry.objects.get(id=115)
            print(main)

            # main=main
            # sub=sub
            # end=end

            cat = catugry.objects.get_or_create(
                name=name ,
                main=main
                # sub_id=44
                # end=end
                )

        self.stdout.write(self.style.SUCCESS('Data imported successfully'))








# jops and service =[
#             'Workers and Technicians' ,
#             'Drivers & Delivery' ,
#             'Sales' ,
#             'Marketing and Public Relations' ,
#             'Tourism, Travel & Hospitality' ,
#             'Guards and Security' ,
#             'Accounting, Finance & Banking' ,
#             'Engineering' ,
#             'Medical, Healthcare, & Nursing' ,
#             'Secretarial' ,
#             'Customer Service & Call Center' ,
#             'Education' ,
#             'Designers' ,
#             'IT - Telecom' ,
#             'Management & Consulting' ,
#             'Legal - Lawyers' ,
#             'HR' ,
#             'Other Job'  ,
#             'Home' ,
#             'Other Services' ,
#             'Business' ,
#             'Medical' ,
#             'Education' ,
#             'Movers' ,
#             'Car' ,
#             'Events' ,
# #             'Health & Beauty' ,
# #             'Pets' ,
#   'Other Business, Industrial & Agriculture' ,
#             'Restaurants Equipment' ,
#             'Industrial Equipment' ,
#             'Medical Equipment' ,
#             'Office Furniture & Equipment' ,
#             'Whole Business for Sale',
#             'Construction',
#             'Agriculture',


#                     ]

#   clothe =[
#             'Women’s Accessories - Cosmetics - Personal Care' ;
#             'Men’s Accessories - Personal Care' ;
#             'Women’s Clothing' ;
#             'Men’s Clothing' ;
#                     ]


#  baby =[
#             'Baby Clothing' ,
#             'Toys' ,
#             'Cribs - Strollers - Carriers' ,
#             'Other Baby Items' ,
#             'Baby Feeding Tools',
#             'Baby & Mom Healthcare',
#                     ]

#  animal =[
#             'Hunting and guard dogs',
#                 'Birds - Pigeons' ,
#                 'Cats' ,
#                 'Other Pets & Animals' ,
#                 'Accessories - Pet Care Products' ,
#                     ]




# Home_Appliances =[
#                 'Air conditioners & Fans',
#                 'Other Home Appliances',
#                 'Refrigerators - Freezers',
#                 'Washers - Dryers',
#                 'Ovens - Microwaves',
#                 'Cooking Tools',
#                 'Heaters',
#                 'Water Coolers & Kettles' ,
#                 'Cleaning Appliances',
#                 'Dishwashers',
#                     ]


















# electronic =[
#                     'Computers - Accessories',
#                     'Video games - Consoles ',
#                     'TV - Audio - Video',
#                     'Cameras - Imaging',

#                     ]
        




#  Properties=[
#             'Apartments & Duplex for Sale',
#             'Apartments & Duplex for Rent',
#             'Buildings & Lands',
#             'Villas For Sale',
#             'Commercial for Rent',
#             'Commercial for Sale',
#             'Vacation Homes for Sale',
#             'Villas For Rent',
#             'Vacation Homes for Rent'
#                     ]
        




# car_model=[

#             'Hyundai',
#             'Fiat',
#             'Chevrolet',
#             'Kia',
#             'Mitsubishi',
#             'Daewoo',
#             'Nissan',
#             'Toyota',
#             'Mercedes-Benz',
#             'Suzuki',
#             'Renault',
#             'Skoda',
#             'Peugeot',
#             'BMW',
#             'Opel',
#             'Volkswagen',
#             'Speranza',
#             'Lada',
#             'Geely',
#             'BYD',
#             'Jeep',
#             'Other make', 
#             'Honda',
#             'Mazda',
#             'Chery',
#             'Daihatsu',
#             'Seat',
#             'Ford',
#             'Citroen',
#             'Isuzu',
#             'Brilliance',
#             'Proton',
#             'MG',
#             'Volvo',
#             'Audi',
#             'Land Rover',
#             'Subaru',
#             'Jac',
#             'Changan',
#             'Chrysler',
#             'MINI',
#             'Senova',
#             'Dodge',
#             'Zotye',
#             'Saipa',
#             'Changhe',
#             'Alfa Romeo',
#             'Jaguar',
#             'Porsche',
#             'Chana',
#             'Faw',
#             'Lifan',
#             'Buick',
#             'Lancia',
#             'Hummer',
#             'Cadillac',
#             'Lincoln' ,
#             'Infiniti',
#             'Maserati',
#             'Bentley',
#             'Lexus',
#             'Ferrari',
#             'Bugatti',
#                     ]

# furniture=[
#             'Bedroom',
#             'Multiple/Other Furniture',
#             'Living Room',
#             'Kitchen - Kitchenware',
#             'Home Decoration',
#             'Dining Room',
#             'Fabrics - Curtains - Carpets',
#             'Garden - Outdoor',
#             'Lighting Tools',
#             'Bathroom',
#                     ]
