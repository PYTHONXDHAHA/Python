import time
import requests
from requests.exceptions import RequestException
from requests.exceptions import SSLError
from requests.exceptions import ChunkedEncodingError
from time import sleep
from proxymanager import ProxyManager
from fake_useragent import UserAgent
from fake_useragent.errors import FakeUserAgentError
import sys
import names
import cloudscraper
from OpenSSL.SSL import Error as OSSLError
from polling import TimeoutException as PTE
import json


password = "test1234"

if len(sys.argv) != 3:
    print("format: python nakedcph_acct_gen.py <emails> <proxies>")
    sys.exit(1)
p = ProxyManager(sys.argv[2])
if len(p.proxies) == 0:
    p = ProxyManager()


while len(emails) > 0:
    email = emails[0]
    if len(email) == 0:
        emails.remove(email)
        continue
    s.cookies.clear()
    print("Creating account for {}".format(email))
    proxy = p.random_proxy().get_dict()

    url = 'https://www.nakedcph.com'
    h = headers
    try:    
        response = s.get(url, headers=h, proxies=proxy)
        print("igenom cloudflare...")
        url = 'https://www.nakedcph.com/auth/view?op=register'
       
            if result['StatusCode'] == 500 and result['Status'] == 'fel':
                print("error: {}".format(result['Status']))
                print("retrying {}...".format(email))
            else:
                print("du har redan acc {}, skippar".format(email))
                emails.remove(email)
        except json.decoder.JSONDecodeError as e:
            print("error creating account: {}".format(t))
            if response.status_code == 429:
                print("proxy kanske bannad...")
            continue
    else:
        print("successful acct for {}".format(email))
        emails.remove(email)
    time.sleep(1)
