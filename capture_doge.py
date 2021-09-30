from bs4 import BeautifulSoup as soup
import requests
import webbrowser
from selenium import webdriver
from datetime import datetime as dt,timedelta
import pywhatkit as kit
import re




chrome = webdriver.Chrome('C:/Users/vishu/ML_projects/webdriver/driver.exe')
#here we use driver.exe in path but it works fine in jupyter even if we just write driver in the end...mean just the name of the chromedriver


address = 'https://wazirx.com/exchange/XRP-INR'

chrome.get(address)

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}

web = requests.get(address, headers=headers)

webSoup = soup(web.text, 'html.parser')

chrome.find_element_by_xpath("//div/input[@class = 'currency-search sc-eqIVtm ivjPmr']").send_keys('doge')

# path = chrome.find_element_by_xpath("//div/a/div[3]/div/span[@class = 'price-text ticker-price' ]")

# path = webSoup.find_all(class_ = 'sc-iELTvK bZNgpE')

price = chrome.find_element_by_class_name('price-box ')
name = chrome.find_element_by_class_name('market-name')
time = dt.now().time()

namex = name.text
pricex = price.text

prc = int(re.search('[0-9]+', pricex).group(0))
print(prc)
print(type(prc))

print(namex, '=', pricex, 'time = ', time)

if prc >= 45:
    now = dt.now()
    time = now.strftime("%M")
    hour = now.strftime("%H")
    print("time:", time)

    hourint = int(hour)
    minuteint = int(time)
    plusminute = minuteint + 2

    print('bawe 45 k uper chala gya h')
    kit.sendwhatmsg('+91' + '7526952513', '45 k uper hai bawa..dkh lo kya krna hai', hourint, plusminute)



elif prc <= 42:
    now = dt.now()
    time = now.strftime("%M")
    hour = now.strftime("%H")
    print("time:", time)
    hourint = int(hour)
    minuteint = int(time)

    plusminute = minuteint + 2

    print('bawe 42 k neche chala gya h')
    kit.sendwhatmsg('+91' + '7526952513', '42 k neche h bawa...dkh lo kya scene hai', hourint, plusminute)






elif prc <= 38:
    now = dt.now()
    time = now.strftime("%M")
    hour = now.strftime("%H")
    print("time:", time)
    hourint = int(hour)

    minuteint = int(time)

    plusminute = minuteint + 2

    print('bawe 38 k uper chala gya h')
    kit.sendwhatmsg('+91' + '7526952513', '38 k neche hai abi toh khreed e lena chaiye tha', hourint, plusminute)



