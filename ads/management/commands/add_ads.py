import datetime
import random
from django.core.management.base import BaseCommand
from ads.models import catugry , ads





class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        for p in range (700000 , 900000 ) :

            main=catugry.objects.get(id=43)
            cat = ads.objects.create(
                title= 'test from command' + str(p),
                description='test from command',
                main=main
                )
            self.stdout.write(self.style.SUCCESS('Data imported successfully' + str(p) ))