from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FireFoxService
from selenium.webdriver import Firefox
import json

start_url = "https://ru.wikipedia.org/wiki/Xbox_360_S"
needed_url = 'https://ru.wikipedia.org/wiki/Nintendo_3DS'


firefox_service = FireFoxService(executable_path='/Users/your/Path/to/geckodriver')
driver = Firefox(service=firefox_service) 

def find_path(start_url):
    driver.get(start_url)
    links = []
    start_url = start_url
    driver.get(start_url)
    link = driver.find_element("xpath", "//a[@href='/wiki/Electronic_Entertainment_Expo']")
    links.append({
        'text': link.text,
        'url': link.get_attribute('href'),
        'sentence': link.find_element(By.XPATH, "./ancestor-or-self::p[1]").text,
    })
    link.click()
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Virtual Boy"))
        )

        links.append({
        'text': element.text,
        'url': element.get_attribute('href'),
        'sentence': element.find_element(By.XPATH, "./ancestor-or-self::p[1]").text,
    })
        element.click()
        last_url = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Nintendo 3DS"))
        )
        links.append({
        'text': last_url.text,
        'url': last_url.get_attribute('href'),
        'sentence': last_url.find_element(By.XPATH, "./ancestor-or-self::p[1]").text,
    })
        last_url.click()
    except:
        print(f'link was not found or doesn not exist')
        driver.quit()
    return links

links = find_path(start_url)

with open('the_path.json', 'w', encoding='utf-8') as f:
    json.dump(links, f, ensure_ascii=False, indent=4)
