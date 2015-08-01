import os
from requests_oauthlib import OAuth1Session

import requests
from requests_oauthlib import OAuth1

from django.conf import settings


def get_authorization_url():
    request_token_url = settings.POWERSHOP_API_ROOT + 'oauth/request_token'
    client_key = os.environ.get('POWERSHOP_OAUTH_CLIENT_KEY')
    client_secret = os.environ.get('POWERSHOP_OAUTH_CLIENT_SECRET')

    # create an oauth session that can be connected to
    oauth = OAuth1Session(client_key, client_secret=client_secret,
                          callback_uri='flatline://flatline-sot.tk/oauth_callback')

    fetch_response = oauth.fetch_request_token(request_token_url)
    oauth_token = fetch_response.get('oauth_token')
    oauth_token_secret = fetch_response.get('oauth_token_secret')

    return oauth_token, oauth_token_secret

