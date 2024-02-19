import time
from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy

cap: Dict[str, Any] = {
    "platformName": "android",
    "automationName": "UIAutomator2",
    "deviceName": "android",
    "appPackage": "com.hmh.api",
    "appActivity": ".ApiDemos",
    "language": "en",
    "locale": "US"

}

url = 'http://localhost:4723'

# Scrolling in view Horizontally
driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))
driver.implicitly_wait(50)

if driver.find_element(by=AppiumBy.XPATH, value="//android.widget.Button[@text='Continue']").is_displayed():
    driver.find_element(by=AppiumBy.XPATH, value="//android.widget.Button[@text='Continue']").click()
    el1 = driver.find_element(by=AppiumBy.ID, value="android:id/button1")
    el1.click()
el2 = driver.find_element(by=AppiumBy.XPATH,
                          value="//android.widget.TextView[@resource-id='android:id/text1' and @text='App']")
el2.click()
el3 = driver.find_element(by=AppiumBy.XPATH,
                          value="//android.widget.TextView[@resource-id='android:id/text1' and @text='Alert Dialogs']")
el3.click()
el4 = driver.find_element(by=AppiumBy.ID, value="com.hmh.api:id/two_buttons")
el4.click()
# el5 = driver.find_element(by=AppiumBy.ID, value="android:id/button1")
# el5.click()       # click on Ok

driver.switch_to.alert.accept()  # click on Ok
# driver.switch_to.alert.dismiss()     # click on Cancel


