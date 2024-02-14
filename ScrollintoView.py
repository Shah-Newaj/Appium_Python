import time
from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy

cap:Dict[str, Any]={
    "platformName": "android",
    "automationName": "UIAutomator2",
    "deviceName": "android",
    "appPackage": "com.hmh.api",
    "appActivity": ".ApiDemos",
    "language": "en",
    "locale": "US"

}

url = 'http://localhost:4723'

# add new contacts using recorded script
driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))
driver.implicitly_wait(50)

if driver.find_element(by=AppiumBy.XPATH, value="//android.widget.Button[@text='Continue']").is_displayed():
    driver.find_element(by=AppiumBy.XPATH, value="//android.widget.Button[@text='Continue']").click()
    el5 = driver.find_element(by=AppiumBy.ID, value="android:id/button1")
    el5.click()
el6 = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[@resource-id='android:id/text1' and @text='App']")
el6.click()
el7 = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[@resource-id='android:id/text1' and @text='Activity']")
el7.click()

driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable('
                                                  'true)).scrollIntoView(new UiSelector().text("Wallpaper"))')
