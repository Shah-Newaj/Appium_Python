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

# Scrolling in view Horizontally
driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))
driver.implicitly_wait(50)

if driver.find_element(by=AppiumBy.XPATH, value="//android.widget.Button[@text='Continue']").is_displayed():
    driver.find_element(by=AppiumBy.XPATH, value="//android.widget.Button[@text='Continue']").click()
    el1 = driver.find_element(by=AppiumBy.ID, value="android:id/button1")
    el1.click()
el2 = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[@resource-id='android:id/text1' and @text='Views']")
el2.click()
el3 = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[@resource-id='android:id/text1' and @text='Gallery']")
el3.click()
el4 = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[@resource-id='android:id/text1' and @text='1. Photos']")
el4.click()

# Method 1
driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable('
                                                  'true)).setAsHorizontalList().scrollToEnd(5)')
driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable('
                                                  'true)).setAsHorizontalList().scrollToBeginning(5)')


# Method 2
# driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable('
#                                                   'true)).setAsHorizontalList().scrollForward(5)')
# driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable('
#                                                   'true)).setAsHorizontalList().scrollBackward(5)')