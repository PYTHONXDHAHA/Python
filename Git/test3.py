# coding=utf-8
import names, time, random
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC


class Accountgen:
    def __init__(self):
        self.proxyCounter = 1

    def proxies(self):
        proxy = {'address': 'pr.smtproxies.com:7777',
                 'username': 'customer-jonathan-cc-SE-asn-3301-sessid-{}'.format(self.proxyCounter),
                 'password': 'jonathan123'}

        capabilities = dict(DesiredCapabilities.CHROME)

        capabilities['proxy'] = {'proxyType': 'MANUAL',
                                 'httpProxy': proxy['address'],
                                 'ftpProxy': proxy['address'],
                                 'sslProxy': proxy['address'],
                                 'noProxy': '',
                                 'class': "org.openqa.selenium.Proxy",
                                 'autodetect': False}

        capabilities['proxy']['socksUsername'] = proxy['username']
        capabilities['proxy']['socksPassword'] = proxy['password']

        self.proxyCounter += 1
        # return capabilities

    def AccGen(self):
        desktop = [
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36",
            "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36",
            "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 UBrowser/6.1.2909.1022 Safari/537.36",
            "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36",
            "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 UBrowser/6.1.2909.1022 Safari/537.36",
            "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 UBrowser/6.0.1471.813 Safari/537.36",
        ]
        # -----------------------------------

        # *************Static***************
        prefs = {"profile.managed_default_content_settings.images": 1}
        options = Options()
        options.add_argument('--disable-gpu')
        options.add_argument("--disable-extensions")
        options.add_argument('--disable-notifications')
        options.add_experimental_option("prefs", prefs)
        options.add_argument("--user-agent={}".format(random.choice(desktop)))
        options.add_argument("--start-maximized")
        options.add_argument("--window-size=1920,1080")
        browser = webdriver.Chrome(executable_path='./chromedriver.exe', desired_capabilities=self.proxies(),
                                   chrome_options=options)
        browser.implicitly_wait(10)

        # ------------------------------------

        # Gå till sidan
        browser.get(
            "https://accounts.google.com/SignUp?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ltmpl=default"
        )

        ###################################################################

        firstName = names.get_first_name()
        lastName = names.get_last_name()
        email = '{}.{}{}'.format(firstName, lastName, random.randint(1000, 9999))
        password = 'test1234'

        ###################################################################
        # Skriva in random Name
        WebDriverWait(browser, 20).until(
            EC.visibility_of_element_located(
                (By.XPATH, '//*[@id="firstName"]'))).send_keys(firstName)

        # Skriva in random Last name
        WebDriverWait(browser, 20).until(
            EC.visibility_of_element_located(
                (By.XPATH, '//*[@id="lastName"]'))).send_keys(lastName)

        # Skriva in email
        WebDriverWait(browser, 20).until(
            EC.visibility_of_element_located(
                (By.XPATH, '//*[@id="username"]'))).send_keys(email)

        # Skriva in lösenord
        WebDriverWait(browser, 20).until(
            EC.visibility_of_element_located(
                (By.XPATH, '//*[@id="passwd"]/div[1]/div/div[1]/input'))).send_keys(password)

        # Skriva in bekräftelse lösenord
        WebDriverWait(browser, 20).until(
            EC.visibility_of_element_located(
                (By.XPATH, '//*[@id="confirm-passwd"]/div[1]/div/div[1]/input'))).send_keys(password)

        # Klicka Nästa
        WebDriverWait(browser, 20).until(
            EC.visibility_of_element_located(
                (By.XPATH, '//*[@id="accountDetailsNext"]/span/span'))).click()
        time.sleep(60000)

if __name__ == "__main__":
    Accountgen().AccGen()
