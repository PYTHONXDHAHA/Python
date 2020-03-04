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

api_key = '2captcha'


if len(sys.argv) != 3:
    print("format: test.py <proxies>")
    sys.exit(1)
p = ProxyManager(sys.argv[2])
if len(p.proxies) == 0:
    p = ProxyManager()
s = cloudscraper.create_scraper(
    delay=10,
    recaptcha={
        'provider': '2captcha',
        'api_key': api_key,
        'proxy': True
    }
)

try:
    ua = UserAgent(verify_ssl=False, use_cache_server=False)
    useragent = ua.chrome
except FakeUserAgentError as e:
    useragent = "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/44.0.2403.155 Safari/537.36"


