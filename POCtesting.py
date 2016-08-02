# try:
#     import simplejson as json
# except ImportError:
#     import json
try:
    import simplejson as json
except ImportError:
    import json
import urllib.request
import urllib
import codecs
import datetime
from LASTIDAPP.models import nextid
import time

def getlaststashid():
    reader=codecs.getreader('utf-8')
    #data=json.load(reader(urllib.request.urlopen('http://www.pathofexile.com/api/public-stash-tabs')))
    next_change_id=nextid.objects.order_by('-nextid_time')[0].nextid_id
    previd=next_change_id
    #13172689-14235686-13105704-15470830-14426942
    ttime=time.time()
    while(True):
        if (time.time()>ttime+1):
            ttime=time.time()
            try:
                data=json.load(reader(urllib.request.urlopen('http://www.pathofexile.com/api/public-stash-tabs?id='+next_change_id)))
                next_change_id=data['next_change_id']
                if next_change_id != previd:
                    print(next_change_id+" - "+datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y"))
                    tid=nextid(
                        nextid_id = next_change_id
                    )
                    tid.save()
                    previd = next_change_id
                    if nextid.objects.count()>=100:
                        idlist=nextid.objects.order_by('-nextid_time')[0:100].values_list("pk",flat=True)
                        nextid.objects.exclude(pk__in=list(idlist)).delete()
                else:
                    print("duplicate")
            except urllib.request.URLError as e:
                if hasattr(e, 'reason'):
                    print('We failed to reach a server: '+e.reason)
                elif hasattr(e, 'code'):
                    print('The server couldn\'t fulfill the request: '+e.code)

