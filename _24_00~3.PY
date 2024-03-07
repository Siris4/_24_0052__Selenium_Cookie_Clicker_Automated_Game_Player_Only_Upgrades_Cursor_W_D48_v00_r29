from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def select_language(driver):
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "langSelect-EN"))).click()
# def select_language(driver):
#     # waits for the game to fully load to ensure elements are clickable
#     time.sleep(5)  # Adjust based on actual load times
#     language_selection = driver.find_element(By.ID, "langSelect-EN")
#     language_selection.click()

def setup_driver():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get("https://orteil.dashnet.org/cookieclicker/")
    return driver


def click_cookie(driver, duration=2):
    cookie = driver.find_element(By.ID, "bigCookie")
    for _ in range(200):
        cookie.click()
    # end_time = time.time() + duration
    # while time.time() < end_time:
    #     driver.find_element(By.ID, "bigCookie").click()

def check_and_click_upgrades(driver, upgrade_xpaths):
    for name, xpath in reversed(upgrade_xpaths.items()):
        try:
            upgrade_element = driver.find_element(By.XPATH, xpath)
            # Add logic here to check if the upgrade is affordable
            upgrade_element.click()
            print(f"Clicked on upgrade: {name}")
            break  # Break after clicking an affordable upgrade
        except NoSuchElementException:
            print(f"Upgrade not found: {name}")
        except ElementClickInterceptedException:
            print(f"Unable to click on upgrade: {name}")

driver = setup_driver()
select_language(driver)  # Now select_language is called after driver is defined


# defines my upgrades"

upgrade_XPATHS = {
    'YOU_UPGRADE': '//*[@id="product19"]',
    'CORTEX_BAKER': '//*[@id="product18"]',
    'IDLEVERSE': '//*[@id="product17"]',
    'JAVASCRIPT_CONSOLE': '//*[@id="product16"]',
    'FRACTAL_ENGINE': '//*[@id="product15"]',
    'CHANCEMAKER': '//*[@id="product14"]',
    'PRISM': '//*[@id="product13"]',
    'ANTIMATTER_CONDENSER': '//*[@id="product12"]',
    'TIME_MACHINE': '//*[@id="product11"]',
    'PORTAL': '//*[@id="product10"]',
    'ALCHEMY_LAB': '//*[@id="product9"]',
    'SHIPMENT': '//*[@id="product8"]',
    'WIZARD_TOWER': '//*[@id="product7"]',
    'TEMPLE': '//*[@id="product6"]',
    'BANK': '//*[@id="product5"]',
    'FACTORY': '//*[@id="product4"]',
    'MINE': '//*[@id="product3"]',
    'FARM': '//*[@id="product2"]',
    'GRANDMA': '//*[@id="product1"]',
    'CURSOR': '//*[@id="product0"]',
}


while True:
    click_cookie(driver, duration=1)  # Adjust duration as needed
    check_and_click_upgrades(driver, upgrade_XPATHS)
    # Adjust the sleep time as necessary based on your needs
    time.sleep(0.1)
