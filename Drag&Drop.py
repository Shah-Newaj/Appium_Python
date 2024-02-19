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
    "appPackage": "com.mobeta.android.demodslv",
    "appActivity": ".Launcher",
    "language": "en",
    "locale": "US"

}

url = 'http://localhost:4723'

# Drag & Drop from one position to another
driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))
driver.implicitly_wait(50)

driver.find_element(by=AppiumBy.XPATH, value='//android.widget.Button[@resource-id="com.android.permissioncontroller:id/continue_button"]').click()
driver.find_element(by=AppiumBy.ID, value='android:id/button1').click()

driver.find_element(AppiumBy.XPATH, value='//android.widget.TextView[@text="Basic usage playground"]').click()

# to work in list must use common resource id with find_elements.Otherwise it will not work
element = driver.find_elements(AppiumBy.XPATH, value='(//android.widget.ImageView[@resource-id="com.mobeta.android.demodslv:id/drag_handle"])')

actions = TouchAction(driver)
actions.press(element[0]).wait(3000).move_to(element[5]).perform().release()    # Drag & Drop from one position to another