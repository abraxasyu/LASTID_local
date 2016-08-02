from django.core.management.base import BaseCommand, CommandError
from LASTIDAPP.models import nextid
#import LASTID
from POCtesting import getlaststashid

class Command(BaseCommand):
    def add_arguments(self,parser):
        parser.add_argument('--update',dest='update',action='store_true',default=False)
        parser.add_argument('--clear',dest='clear',action='store_true',default=False)
        parser.add_argument('--last',dest='last',action='store_true',default=False)
    def handle(self, *args, **options):
        if options['update']:
            getlaststashid()
        elif options['clear']:
            nextid.objects.all().delete()
            print("all nextids deleted")
        elif options['last']:
            print(nextid.objects.order_by('-nextid_time')[0].nextid_id)
