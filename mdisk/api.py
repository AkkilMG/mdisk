
# Author: heimanpictures (Akkil)
# Project: Mdisk Unofficial API
# Copyrights (c) by heimanpictures (Akkil)


import requests
import re
import sys

class Mdisk:
    '''
    Python mdisk api wrapper from official bot (@)
    
    all method below return dict that contain info
    '''
    
    base_url = "https://diskuploader.mypowerdisk.com/v1/tp/cp"
    
    def __init__(self, api_key):
        '''
        init mdisk
        
        Args:
            api_key (str): api key from mdisk
        '''
        self.api_key = api_key
  
    def upload(self, link):
        '''
        Upload files using direct links
        
        Args:
            link (str): link from site to get streaming link
        '''
        try:
            param = {'token':str(self.api_key), 'link':str(link)} 
            r = requests.post(url, json = param) 
            response = r.json()
            mdisk = response["sharelink"]
            return mdisk
        except ConnectionError as e:
            sys.exit(f"ERROR : {e}")

          
