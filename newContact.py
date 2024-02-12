import time

from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy

cap:Dict[str, Any]={
    "platformName": "android",
    "automationName": "UIAutomator2",
    "deviceName": "android",
    "appPackage": "com.google.android.contacts",
    "appActivity": "com.google.android.apps.contacts.activities.PeopleActivity",
    "language": "en",
    "locale": "US"

}

url = 'http://localhost:4723'

# add new contacts
driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))
driver.implicitly_wait(50)
# time.sleep(10)
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Create contact').click()

driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@text="First name"]').send_keys('Shah')
driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@text="Last name"]').send_keys('Newaj')
driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@text="Phone"]').send_keys('01741')
driver.find_element(by=AppiumBy.ID, value='com.google.android.contacts:id/toolbar_button').click()

# driver.quit()