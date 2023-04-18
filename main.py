

driver = None
wait = None

username = ""
password = ""

threads = [
    "https://flipd.gg/Thread-%E2%80%BC%E2%AD%90REALLY-CHEAPEST-RANKS-RANKED-READY-ACCOUNTS-%E2%AD%90%E2%80%BC-DC-treppi-9999",
    "https://flipd.gg/Thread-EU-NA-BEST-PRICES-ASCENDANT-IMMORTAL-ACCOUNTS",
    "https://flipd.gg/Thread-NA-PUBLIC-BETA-ACCESS-PRIME-KARAMBIT-25",
    "https://flipd.gg/Thread-%E2%AD%90BEST-PRICE-RANKED-SHOP%E2%AD%90Quick-delivery-DC-treppi-9999",
    "https://flipd.gg/Thread-%E2%80%BC%E2%AD%90Ranked-Smurf-Accounts%E2%AD%90%E2%80%BC-DC-treppi-9999",
    "https://flipd.gg/Thread-NA-Endeavour-Set-Radiant-Crisis-Phantom-Ion-Sheriff-Battlepass-Skins-FA-35",
    "https://flipd.gg/Thread-EU-TUR-Yoru-Butterfly-Knife-Forsaken-Vandal-Prime-Phantom-SYS-Set-35",
    "https://flipd.gg/Thread-EU-VCT-Lock-Knife-Chronovoid-Elderflame-Vandal-Sentinels-of-Light-OP-85"
]

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import undetected_chromedriver as uc
from os import system



system("title flipd autobump")

def startDriver():
    print("starting driver")
    global driver
    chrome_options = Options()
    chrome_options.add_argument('--disable-blink-features=AutomationControlled')
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36")
    driver = uc.Chrome(use_subprocess=True,options=chrome_options)
    global wait
    wait = WebDriverWait(driver, 20) 


def login():
    print("logging in...")
    driver.get("https://flipd.gg/login")
    sleep(10)
    input("#fullcontainment > div > form:nth-child(3) > table > tbody > tr.tr-rounded > td > label > input", username)
    sleep(1)
    input("#fullcontainment > div > form:nth-child(3) > table > tbody > tr:nth-child(2) > td > label > input", password)
    sleep(1)
    click("#fullcontainment > div > form:nth-child(3) > table > tbody > tr:nth-child(4) > td > span > input")
    sleep(3)



def bump(threadurl, message):
    print(f"bumping {threadurl}!")
    driver.get(threadurl)
    sleep(8)
    input("#message", message)
    click("#quick_reply_submit")
    print("bumped!!")
    sleep(4)
    driver.quit()


def input(element, message):
    print("looking for "+element)
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, element))).send_keys(message)
    print("found "+element)

def click(element):
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, element))).click()

def sleep(t):
    while t > 0:
        time.sleep(1)
        t -= 1
        print(t)

def getMessage():
    current_time = time.strftime("%H:%M:%S", time.localtime())
    return f"{current_time} | message me on discord: treppi#9999"



bump_delay = 60*7


for threadurl in threads:
    startDriver()
    login()
    bump(threadurl, getMessage())
    print(f"waiting {bump_delay} seconds to bump again...")
    sleep(bump_delay)



































