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

# add new contacts using recorded script
driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))
driver.implicitly_wait(50)

driver.find_element(by=AppiumBy.ID, value='android:id/button2').click()
driver.find_element(by=AppiumBy.ID, value='com.android.permissioncontroller:id/permission_allow_button').click()

el5 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Create contact")
el5.click()
el6 = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.EditText[@text=\"First name\"]")
el6.send_keys("newaj3")
el7 = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.EditText[@text=\"Phone\"]")
el7.send_keys("98765")
el8 = driver.find_element(by=AppiumBy.ID, value="com.google.android.contacts:id/toolbar_button")
el8.click()
