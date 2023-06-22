import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE' , 'intern.settings')
import django
django.setup()
import pandas as pd
from app.models import Restaurants

import json
df=pd.read_csv('restaurants_small.csv')


row_iter = df.iterrows()



# row = json.loads(df.loc[0,'items'])

# print(type(row))

objs = [

    Restaurants(

        id = df.loc[i,'id'],

        name  = df.loc[i,'name'],

        location  = df.loc[i,'location'],

        items  = json.loads(df.loc[i,'items'])

    )

    for i in range(len(df))

]
Restaurants.objects.bulk_create(objs)

