from requests import get
from time import sleep
from random import randint

while True:
    x = get('https://ac70484e-ccd3-43c8-9dda-05868b6deee2-00-19q8692yqmsid.kirk.replit.dev/')
    n = randint(5,100)
    sleep(n*6)

