# -*- coding: utf-8 -*-
import urllib2
import json
from city import city

'''
web = urllib2.urlopen('http://www.baidu.com')
content = web.read()
print content
'''
cityname = raw_input('enter the city:')
citycode = city.get(cityname)
if citycode:
   url = 'http://www.weather.com.cn/data/cityinfo/%s.html' % citycode
   req = urllib2.Request(url)
   res_data = urllib2.urlopen(req)
   res = res_data.read()
   data = json.loads(res)
   #print type(res)
   #print type(data)

result = data['weatherinfo']
str_temp = ('%s\n%s ~ %s') % (
   result['weather'],
   result['temp1'],
   result['temp2']
)
print str_temp
