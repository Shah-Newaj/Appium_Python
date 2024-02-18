import time

from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction

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

# Tap and Long Press
driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))
driver.implicitly_wait(50)

driver.find_element(by=AppiumBy.ID, value='android:id/button2').click()
driver.find_element(by=AppiumBy.ID, value='com.android.permissioncontroller:id/permission_allow_button').click()


# need to use variable to store index, and find_elements to indicate index through variable, and resource id as xpath otherwise it wil not work
element = driver.find_elements(AppiumBy.XPATH, value='//android.widget.TextView[@resource-id="com.google.android.contacts:id/cliv_name_textview"]')
print(len(element))

actions = TouchAction(driver)
# actions.tap(element[1]).perform().release()           # Single Tap
actions.long_press(element[1]).perform().release()      # Long Tap
