from requests_oauthlib import OAuth1Session
import json
from flatline.models import Bill, Flat
from datetime import datetime

def test():
    resource_owner_key = "e40cf7ea7dbe049f9e9c2c899b2e10c9"
    resource_owner_secret = "44a9426a642eb178dc9d19ebdc31227e"
    client_key = "742ea45f6dd448ba5098c4839b13be0c"
    client_secret = "PR2tdqgNHG7zt7H2tWlK4h31t48knQum"

    powershop = OAuth1Session(client_key,
                              client_secret=client_secret,
                              resource_owner_key=resource_owner_key,
                              resource_owner_secret=resource_owner_secret)

    header = {'content-type': 'application/javascript'}
    url = 'https://wip5.test.powershop.co.nz/external_api/v1/billings.js?icp_number=0000129785TR238'

    content = powershop.get(url, headers=header).content

    resp = json.loads(content)

    bills = resp['result']['billings']


    flat = Flat.objects.get(pk=1)

    for bill in bills:
        cost = bill['value']
        cost_per = cost/4.0

        Bill.objects.create(start=datetime.now(), end=datetime.now(), cost=cost, flat=flat, cost_per_user=cost_per)

    return bills
