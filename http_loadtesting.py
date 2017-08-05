#!/usr/bin/python3
"""
This script will load test a URL and will print errors when they occur.

Example use:

python3 http_loadtesting.py -a http://10.155.21.220 --host nginx.com -w 500


"""
import time
import datetime
import sys
import logging
from concurrent import futures
import itertools
import requests
import functools
import aiohttp
import asyncio
import async_timeout
import os
import argparse
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


def http_get(config_args):
    """
    Function that makes a test HTTP get request.
    """
    #global config_args
    
    
    try:
    #r = requests.get(config_args.address,headers=headers,verify=config_args.cacert)
        if 'https' in config_args.address.lower() and config_args.host != None:
            headers = {'host': config_args.host}
            r = requests.get(config_args.address,headers=headers,verify=False)
            #print(config_args.address.lower())
        elif 'https' in config_args.address.lower() and config_args.host == None:
            r = requests.get(config_args.address,verify=False)
            print(config_args.address.lower())
        else:
            r = requests.get(config_args.address)

        if r.status_code != 200 and r.status_code != 301 and r.status_code != 302:
            print("Request failed...code: {}".format(r.status_code))
    except KeyboardInterrupt:
            print ('Stopping now....')
            try:
                sys.exit(0)
            except SystemExit:
                os._exit(0)    
    
    return r


def main():

    parser = argparse.ArgumentParser(description="Arguments for testing a URL.")
    parser.add_argument('--host', required=False, action='store',help='Value to be populated for the host header')
    parser.add_argument('-a', '--address', required=True, action='store',help='ip address')
    #parser.add_argument('-ca', '--cacert', required=False, action='store',help='Path to ca cert')
    parser.add_argument('-w', '--workers', required=True, action='store',help='Number of workers')

    #global config_args
    config_args = parser.parse_args()

    executor = futures.ThreadPoolExecutor(max_workers=int(config_args.workers))
    


    while True:
        try:
            results = executor.map(http_get, [config_args])
        except KeyboardInterrupt:
            print ('Stopping now....')
            try:
                sys.exit(0)
            except SystemExit:
                os._exit(0)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print ('Stopping now....')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)