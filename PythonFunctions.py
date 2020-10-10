### author: Johnny
from random import choice

import requests
from bs4 import BeautifulSoup
from requests import Timeout


def get_random_proxy():
    url = 'http://www.sslproxies.org/'
    req = requests.get(url)
    # convert it to this object for easy parsing
    soup = BeautifulSoup(req.content, 'html5lib')
    # get a list of tuple of each items with it's ip_addr and port num
    result = list(map(lambda x: x[0] + ':' + x[1], list(zip(map(lambda x: x.text, soup.findAll('td')[::8]),
                                                            map(lambda x: x.text, soup.findAll('td')[1::8])))))
    result = choice(map(lambda x: x.encode('ascii'), result)[:20])
    return result


def proxy_request(request_type, url, **kwargs):
    while 1:
        try:
            p = get_random_proxy()
            proxy = {'http': p, 'https': p}
            print('using proxy: {}'.format(proxy))
            req = requests.request(request_type, url, proxies=proxy, timeout=2, **kwargs)
            break
        except Timeout:
            print 'waiting too long'
        except requests.exceptions.ProxyError:
            print 'Proxy Error, could not connect'
            pass
        except requests.exceptions.HTTPError:
            print 'request exception HTTP error'
            pass
    return req


def main():
    r = proxy_request("get", "https://api.myip.com")
    print(r.status_code)
    print(r.content)


if __name__ == '__main__':
    main()
