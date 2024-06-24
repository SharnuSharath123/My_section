import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'second_project.settings')

import django
django.setup()

# Fake pop script

import random
from second_app.models import AccessRecord, Webpage, Topic
from faker import Faker


fakegen = Faker()
topics = ['Search', 'Social', 'Marketplace', 'News', 'Games']

def add_topic():
    topic = random.choice(topics)
    t, created = Topic.objects.get_or_create(top_name=topic)
    return t

def populate(N=5):

    for entry in range(N):

        # Get the topic for the entry

        top = add_topic()

        # create the fake data for that entry
        fake_url = fakegen.url()
        fake_name = fakegen.company()
        fake_date = fakegen.date()
        

        # create the new webpage entry
        Webpg = Webpage.objects.get_or_create(topic = top, url = fake_url, name = fake_name)


        # create a fake access record for that webpage
        acc_rec = AccessRecord.objects.get_or_create(name = Webpg, date = fake_date)[0]


if __name__ == '__main__':
    print("populating script!")
    populate(20)
    print("populating complete!")


    
