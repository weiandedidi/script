import urllib
import urllib2

url = 'http://www.baidu.com/login'
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
referer = 'http://www.baidu.com'
values = {'username': 'cqc', 'password': 'XXXX'}
headers = {'User-Agent': user_agent,'Referer':referer}
data = urllib.urlencode(values)
request = urllib2.Request(url, data, headers)
response = urllib2.urlopen(request)
page = response.read()
