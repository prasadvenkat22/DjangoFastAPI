
from pandas import json_normalize 
import logging
from dotenv import load_dotenv
import requests
import json
import logging
from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session
import os
import requests
from requests.structures import CaseInsensitiveDict
import time
#logger = logging.getLogger(name="subscriber-to-oi-cache-api")

class OAuthManager:
    def __init__(self) -> None:
        self.client_id = os.getenv("OAUTH_CLIENT_ID_COS_CONSUMER")
        self.client_secret = os.getenv("OAUTH_CLIENT_SECRET_COS_CONSUMER")
        self.oauth_url = os.getenv("OAUTH_URL_COS")
        self.token = None

    @property
    def get_token(self):
        try:
            if self.token is None or (
                self.token is not None
                and self.token.get("expires_at", 0) <= time.time()
            ):
                self.token = self.generate_oauth_token()
            return self.token.get("access_token")
        except Exception as e:
            print(str(e))


    def generate_oauth_token(self):
        """Generate OAuth Bearer token based on client credentials"""
        #logger.info("generate_oauth_token::START")
        try:
            client = BackendApplicationClient(client_id=self.client_id)
            oauth = OAuth2Session(client=client)
            token = oauth.fetch_token(
                token_url=self.oauth_url,
                client_secret=self.client_secret,
            )
            return token
        except Exception as e:
            #logger.error(str(e))
            raise Exception("Invalid credentials.")



class OiCacheManager:
    def get_download_urls(self, token, cpy_key):
        #logger.info('get_download_files::START')
        payload = {}
        url = f"{os.getenv('COS_API_BASE_URL')}/api/v1/s3-download-files?cpy_key={cpy_key}"
        headers = CaseInsensitiveDict()
        #headers={'Authorization': token, 'X-APP-ID':'UP' ,
        # 'X-USER-ID':'vetangir@cisco.com'}

        headers["Authorization"] = f"Bearer {token}"
        headers['X-APP-ID'] = os.getenv('CONSUMER_APP_ID')
        try:
            response = requests.post(url=url, json=payload, headers=headers)
            response.raise_for_status()
            return response
        except Exception as e:
            #logger.error(str(e))
            raise Exception(str(e))

