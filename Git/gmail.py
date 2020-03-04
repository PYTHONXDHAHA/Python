import pyautogui
import sys
import time
import random
import string
import names
import keyboard
import fileinput
import webbrowser
import os
import webbrowser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from threading import Thread

def msg(_option_, _message_):
    if _option_ == 1:
        print('\x1b[0;32;40m> %s\x1b[0m' % _message_)
    elif _option_ == 2:
        print('\x1b[0;32;40m>\x1b[0m %s' % _message_)
    elif _option_ == 3:
        print('\n\x1b[0;32;40m[\x1b[0m%s\x1b[0;32;40m]\x1b[0m' % _message_)
    else:
        print('\n\x1b[0;31;40m[ERROR]\x1b[0m')


def ext():
    msg(1, 'Exiting...')
    sys.exit()


def open_firefox():
 #   msg(1, 'Startar Firefox...')
#
 #   _start_button_ = pyautogui.locateOnScreen('images/start_button.png')
  #  _location_ = pyautogui.center(_start_button_)
#
 #   if not pyautogui.click(_location_):
  #      msg(1, 'Startar menyn!')
   # else:
    #    msg(3, 'Faila att start meny!')
     #   ext()

   # time.sleep(2)

    #pyautogui.typewrite('firefox')
    #pyautogui.typewrite('\n')

    print ('Firefox runnar.')

    #time.sleep(4)
 
      
    
   # url = "google.com"
    #chrome_path = 'C:/Users/Jonathan Lilie/AppData/Local/Google/Chrome/Application/chrome.exe %s --incognito'
    #webbrowser.get(chrome_path).open_new(url)
    #print ("Vanta 1")
    #time.sleep(3)
    #print ("Vanta 2")
    #print ("friefox klar")

hostname = "pr.smtproxies.com"
port = "7777"
proxy_username = "customer-jonathan-cc-SE-asn-3301-sessid-1"
proxy_password = "jonathan123"

chrome_options = Options()
chrome_options.add_argument('--proxy-server={}'.format(hostname + ":" + port))
driver = webdriver.Chrome(options=chrome_options)

print("test1")

def enter_proxy_auth(proxy_username, proxy_password):
    time.sleep(1)
    print("test2")
    pyautogui.typewrite(proxy_username)
    pyautogui.press('tab')
    pyautogui.typewrite(proxy_password)
    pyautogui.press('enter')


def open_a_page(driver, url):
    driver.get(url)


Thread(target=open_a_page, args=(driver, "google.com/")).start()
Thread(target=enter_proxy_auth, args=(proxy_username, proxy_password)).start()

#driver = webdriver.Chrome('C:/Users/Jonathan Lilie/Documents/gmail/gmail-generator-master/source/chromedriver')  # Optional argument, if not specified will search path.
#driver.get('https://accounts.google.com/SignUp?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ltmpl=default');
#time.sleep(5) # Let the user actually see something!



def locate_gmail():
    msg(1, 'Open Gmail...')
    pyautogui.typewrite('https://accounts.google.com/SignUp?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ltmpl=default')
    pyautogui.typewrite('\n')

time.sleep(2)
    #Proxy

def clean():
    msg(1, 'Startar Firefox...')

    msg(1, 'baj')
def locate_proxy():

    f = open("proxy1.txt", "r")
    pyautogui.typewrite(f.read(42))
    print('Första Proxyraden skriven')

    
def locate_proxy2():
    
    with open("proxy1.txt", "r+") as f:
        lines = f.readlines()
        f.seek(0)
        i = 1
        while i < len(lines):
            if(i > 0):
                f.write(lines[i])
            i += 1

        f.truncate()

    print('Tog bort första raden')

def locate_proxy3():
    pyautogui.typewrite('\t')
    pyautogui.typewrite("jonathan123")
    pyautogui.typewrite('\n')




def randomize(
        _option_,
        _length_
):
    if _length_ > 0:

        if _option_ == '-p':
            string._characters_ = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+'
        elif _option_ == '-l':
            string._characters_ = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        elif _option_ == '-n':
            string._characters_ = '1234567890'
        elif _option_ == '-m':
            string._characters_ = 'JFMASOND'

        if _option_ == '-d':
            _generated_info_ = random.randint(1, 28)
        elif _option_ == '-y':
            _generated_info_ = random.randint(1950, 2000)
        else:
            _generated_info_ = ''
            for _counter_ in range(0, _length_):
                _generated_info_ = _generated_info_ + \
                                   random.choice(string._characters_)

        return _generated_info_

    else:
        msg(3, 'Fel längd')
        ext()

  
# Info
def generate_info():
    # SKriver
    msg(1, 'Genererar Namn etc')
    time.sleep(4)

    # För och efternamn
    _first_name_ = names.get_full_name(gender='male')
    pyautogui.typewrite(_first_name_)
    pyautogui.typewrite('\t')
    _last_name_ = names.get_last_name()
    pyautogui.typewrite(_last_name_)
    pyautogui.typewrite('\t')
    msg(2, '\x1b[0;33;40mName:\x1b[0m %s %s' % (_first_name_, _last_name_))

    # Mail
    _username_ = names.get_first_name(gender='male')
    pyautogui.typewrite(_username_)
    _username2_ = names.get_first_name(gender='male')
    pyautogui.typewrite(_username2_)

    _nummer_ = randomize('-n', 4)
    pyautogui.typewrite(_nummer_)
    pyautogui.typewrite('\t')
    msg(2, '\x1b[0;33;40mUsername:\x1b[0m %s%s%s' % (_username_, _username2_, _nummer_))

    file = open("email.txt", "a")
    file.write("{}{}{}@gmail.com \n".format(_username_, _username2_, _nummer_))
    file.close()

    time.sleep(1)

    # Password
    _password_ = "test1234"
    pyautogui.typewrite(_password_ + '\t' + _password_ + '\t' + '\t' + "\n")
    msg(2, '\x1b[0;33;40mPassword:\x1b[0m %s' % _password_)

    # Nummer verify
    msg(1, "Väntar på nummer verify")

    while True:
        try:
            if keyboard.is_pressed('AltGr'):
                print('Finnished Nummer!')
                break
            else:
                pass
        except:
            break

    time.sleep(4)
    print('Väntade 2 Secs!')
    # Datum
    _month_=randomize('-y',1)
    _day_=randomize('-m',1)
    _year_=randomize('-d',1)
    pyautogui.typewrite(_month_+'\t'+str(_day_)+'\t'+str(_year_)+'\t')
    msg(2,'\x1b[0;33;40mDate of birth:\x1b[0m %s/%d/%d' % (_month_,_day_,_year_))

    # Kön
    pyautogui.typewrite('j\t')
    msg(2, '\x1b[0;33;40mGender:\x1b[0m Rather not say')

    # Skippa
    pyautogui.typewrite('\t\t')


if __name__ == '__main__':

    if open_firefox():
        msg(3, 'Failed to execute "open_firefox" command.')
        ext()

    if enter_proxy_auth():
        msg(3, 'Failed to execute "open_firefox" command.')
        ext()
    
    if open_a_page():
        msg(3, 'Failed to execute "open_firefox" command.')
        ext()

 #   if locate_gmail():
  #      msg(3, 'Failed to execute "locate_gmail" command.')
   #     ext()

    #if locate_proxy():
     #   msg(3, 'Failed to execute "locate_proxy" command.')
      #  ext()

    #if locate_proxy2():
     #   msg(3, 'Failed to execute "locate_proxy2" command.')
      #  ext()

    #if locate_proxy3():
     #   msg(3, 'Failed to execute "locate_proxy2" command.')
      #  ext()

 

   # if generate_info():
    #    msg(3, 'Failed to execute "generate_info" command.')
     #   ext()

      #  msg(1, 'Done...')
       # ext()