import time

from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy

cap:Dict[str, Any]={
    "platformName": "android",
    "automationName": "UIAutomator2",
    "deviceName": "android",
    # "appPackage": "com.android.settings",
    # "appActivity": ".Settings",
    "language": "en",
    "locale": "US"

}

url = 'http://localhost:4723'

# This is the first demo
driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))

driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Phone').click()
time.sleep(5)
driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="Recents"]').click()
time.sleep(5)
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='key pad').click()
driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="0"]').click()
driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="8"]').click()
driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="5"]').click()
driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="2"]').click()

driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='dial').click()
time.sleep(25)
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='End call').click()


# driver.quit()