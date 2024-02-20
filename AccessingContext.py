import time
from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

cap: Dict[str, Any] = {
    "platformName": "android",
    "automationName": "UIAutomator2",
    "deviceName": "android",
    "appPackage": "com.socialnmobile.dictapps.notepad.color.note",
    "appActivity": "com.socialnmobile.colornote.activity.Main",
    "language": "en",
    "locale": "US"

}

url = 'http://localhost:4723'

# Accessing Context
driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))
driver.implicitly_wait(50)

wait = WebDriverWait(driver, timeout= 10)

# Click on Allow
el1 = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, "//android.widget.Button[@text='Allow']")))
el1.click()
# Click on Skip
el2 = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, "//android.widget.Button[@text='SKIP']")))
el2.click()
# Click on More
el3 = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, "//android.widget.FrameLayout[@content-desc='More']")))
el3.click()
# Click on FB
el4 = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, "//android.widget.TextView[@text='Like us on Facebook']")))
el4.click()

if driver.find_element(by=AppiumBy.ID, value="com.android.chrome:id/terms_accept").is_displayed():
    driver.find_element(by=AppiumBy.ID, value="com.android.chrome:id/terms_accept").click()
    driver.find_element(by=AppiumBy.ID, value="com.android.chrome:id/negative_button").click()
    driver.find_element(by=AppiumBy.ID, value="com.android.chrome:id/negative_button").click()