#!/usr/bin/python3
"""
This script will load test a URL and will print out errors.

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



def http_test(n):
    global config_args
    headers = {'host': config_args.host}
    r = requests.get(config_args.address,headers=headers,verify=config_args.cacert)
    if r.status_code != 200 and r.status_code != 301:
        print("Request failed...code: {}".format(r.status_code))
    
    return r


def main():
#    async with aiohttp.ClientSession() as session:
    parser = argparse.ArgumentParser(description="arguments for testing HAProxy")

    parser.add_argument('--host', required=True, action='store',help='host header')

    parser.add_argument('-a', '--address', required=True, action='store',help='ip address')

    parser.add_argument('-ca', '--cacert', required=False, action='store',help='ca cert')

    parser.add_argument('-w', '--workers', required=False, action='store',help='number of workers')

    global config_args
    config_args = parser.parse_args()


    executor = futures.ThreadPoolExecutor(max_workers=int(config_args.workers))

    while True:
        try:
            results = executor.map(http_test, range(int(config_args.workers)))
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