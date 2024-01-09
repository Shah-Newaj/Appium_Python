import time

from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy

cap:Dict[str, Any]={
    "platformName": "android",
    "automationName": "UIAutomator2",
    "deviceName": "android"


}

url = 'http://localhost:4723'

# Use of id
driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))

el = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='YouTube')

el.click()
time.sleep(5)

driver.find_element(by=AppiumBy.XPATH, value='//android.widget.ImageView[@content-desc="Search"]').click()
time.sleep(5)
driver.find_element(by=AppiumBy.XPATH, value='//*[@text="Search YouTube"]').send_keys("Merciful Servant")
# driver.quit()