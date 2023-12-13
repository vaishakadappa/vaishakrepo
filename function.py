"""
Script: function1.py
Developed By: Rahul Patel
Developed On:  September 7, 2023

Summary: 
Release 1 - 
This script has been developed to create a function which is going to validate the websites url.
This script will take a file name as input parameter which need to be validate. The function will return
a dataframe in the output.
"""
from urllib.request import urlopen
from urllib.error import URLError, HTTPError
import pandas as pd
import requests
import ssl
import time

def urlvalidate(inputpath):
    # Read the file to be validated in dataframe
    df = pd.read_csv(inputpath, sep="|")

    context = ssl._create_unverified_context()
    #Iterate the dataframe to validate the URL.
    for idx, row in df.iterrows():
        
        print(idx+1, ".", row['url'])
        max_retry=50
        retry_delay=5
        retries=0

        while retries<max_retry:
            try:
                response = urlopen(row['url'], context=context)          
            except HTTPError as e:
            #update the error message
                df.at[idx,'output'] = 'Couldn\'t fulfill the request'
                df.at[idx,'error'] = e.code
            
            except URLError as e:
            #update the error message
                df.at[idx,'output'] = 'Failed'
                df.at[idx,'error'] = e.reason
            else:
                #update the sucess message
                if response.geturl()==row['url']:
                    df.at[idx,'output'] = 'Ok'
                else:
                    df.at[idx,'output'] = 'Ok'
                    df.at[idx,'redirecturl'] = response.geturl()
                break
           
            retries+=1
            
        # 5 second delay to avoid any blockage
        time.sleep(retry_delay)
        
        if retries >=max_retry:
            df.at[idx, 'output'] = 'Failed after retries'
                
    #Remove nan character from dataframe.
    df.fillna('', inplace=True)   
    
    #Return the out in dataframe. 
    return df