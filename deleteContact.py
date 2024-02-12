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

#Skip sign-in and notification
driver.find_element(by=AppiumBy.ID, value='android:id/button2').click()
driver.find_element(by=AppiumBy.ID, value='com.android.permissioncontroller:id/permission_allow_button').click()

driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='newaj3').click()
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='More options').click()
driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="Delete"]').click()
driver.find_element(by=AppiumBy.ID, value='android:id/button1').click()

# driver.quit()