import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','BackendTest.settings')
import django
django.setup()
from django_seed import Seed
from userActivityApp.models import User,ActivityPeriod
import random

i=['ABC234','ABC1123','ABCE12','ABC2378','ABCF123','ABCE1294','AWC2378','ABCF103','ABRE1254']
timezn=['Asia/Kolkata','America/Newyork']
seeder = Seed.seeder()
seeder.add_entity(User, 5,{
    'name': lambda x: seeder.faker.name(),
    'reg_id':lambda x:random.choice(i),
    'tz': lambda x:random.choice(timezn),

})
seeder.add_entity(ActivityPeriod, 10)

inserted_pks = seeder.execute()
