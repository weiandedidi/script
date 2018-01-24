import urllib2

# urllib2 默认会使用环境变量 http_proxy 来设置 HTTP Proxy,设置一些代理服务器来帮助你做工作，每隔一段时间换一个代理
# 代理的代码放置在请求代码之前
enable_proxy = True
proxy_handler = urllib2.ProxyHandler({"http": 'http://some-proxy.com:8080'})
null_proxy_handler = urllib2.ProxyHandler({})
if enable_proxy:
    opener = urllib2.build_opener(proxy_handler)
else:
    opener = urllib2.build_opener(null_proxy_handler)
urllib2.install_opener(opener)
