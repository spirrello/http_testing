#!/usr/bin/env python3

"""This script will measure load times for several sites."""


import requests
import time
from datetime import datetime
from datetime import timedelta


def calc_time(start_time):
   """This method will calculate the time for rendering a web page."""
   dt = datetime.now() - start_time
   ms = (dt.days * 24 * 60 * 60 + dt.seconds) * 1000 + dt.microseconds / 1000.0
   return int(ms)

def measure_sites():
    """This meathod is invoked from our HTML page"""
    sites = ['http://www.cnn.com/','http://www.espn.com/','https://www.facebook.com/','http://www.foxnews.com','https://www.yahoo.com/']
    site_list = [['Sites','Latency']]
    #Loop through the list of sites and print the page load time.
    x = 0
    for site in sites:
        
        start_time = datetime.now()
        r = requests.get(site)
        load_time = calc_time(start_time)
        #print(site + " loaded in " + str(load_time) + " ms")
        #Need to clean up the sites list.
        sites[x] = sites[x].replace("http://", "")
        sites[x] = sites[x].replace("https://", "")
        sites[x] = sites[x].replace("www", "")
        sites[x] = sites[x].replace("/", "")
        sites[x] = sites[x].replace(".com", "")
        sites[x] = sites[x].replace(".", "")
        site_list.append([sites[x],load_time])
        x +=1

    
    return site_list


def main():

    print ("Content-type: text/html")
    
    web_page="""
    <h1>Google Charts with Python</h1>
    <meta http-equiv="refresh" content="10">
    <script type="text/javascript" src="https://www.google.com/jsapi"></script>
    <script type="text/javascript">
      google.load("visualization", "1", {packages:["corechart"]});
      google.setOnLoadCallback(drawChart);
      function drawChart() {
        var data = google.visualization.arrayToDataTable("""+ str(measure_sites()) +""");

     var options = {
        title: 'HTTP Latency',
        chartArea: {width: '50%'},
        hAxis: {
          title: 'Milliseconds',
          minValue: 0
        },
        vAxis: {
          title: 'Sites'
        }
      };

      var chart = new google.visualization.BarChart(document.getElementById('chart_div'));
        chart.draw(data, options);
      }
    </script>
    <div id="chart_div"></div>

    </body>
    """
    print (web_page)



if __name__=="__main__":
    main()


