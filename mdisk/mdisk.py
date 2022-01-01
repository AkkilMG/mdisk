
# Author: heimanpictures (Akkil)
# Project: Mdisk Unofficial API
# Copyrights (c) by heimanpictures (Akkil)


import click
import os
import sys
from mdisk import mdisk

api = os.environ.get("MDISK_API")
d = Mdisk(api)

@click.group()
def main():
    '''mdisk free video hosting cli'''
    if api == None or len(api) == 0:
        print("Please set mdisk api key in environment variable first")
        print("$ export MDISK_API=your_key_here")
        sys.exit()
        
      
@main.command()
@click.argument("link")
def upload(link):
    '''upload from link'''
    if "http://" in link or "https://" in link:
        md_link = d.upload(link)
        print("#"*10 + " Upload " + "#"*10)
        print(f"Link : {md_link}")
        print("")
        print("#"*40)
    else:
        print("#"*10 + " Remote Upload " + "#"*10)
        print("\nPlease add http:// or https:// in link\n")
        print("#"*40)
        
        
