# Python scripts for load testing URLs and measuring latency.

## http_loadtesting.py

This script can load test a site and print HTTP 400 and 500 errors.

python3 http_loadtesting.py -a http://[ip or domain] --host [optional host header] -w [number of workers]


## measure_sites.py

This script will check latency using HTTP get requests and generate results using Google charts.
