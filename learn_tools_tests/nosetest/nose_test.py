from nose.tools import *
from selenium import webdriver
 # nosetests -v nose_test.py
"""______________________________________________________________________________________________________________________"""

# Logic on Home Page
class homePage(object):

    def __init__(self, driver):
        self.driver = driver
    # click button by xpath and contains text
    def clickButton(self, button):
        self.driver.find_element_by_xpath('//*[1][contains(text(), "%s")]' % button).click()
        return True

"""______________________________________________________________________________________________________________________"""

# Logic on Term and Condition Page
class termsAndConditionsPage(object):

    # Logic before test
    def __init__(self, driver):
        self.driver = driver

    # check presents of text by xpath and contains text
    def presentText(self, text):
        self.driver.find_element_by_xpath('//*[contains(text(), "%s")]' % text)
        return True
"""______________________________________________________________________________________________________________________"""

# Test Cases
class TestCases:

    # Logic before test
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://demo.icons8.com")
        self.driver.implicitly_wait(10)
        print ("Test start")

    # Logic after test
    def teardown(self):
        print ("Test end")
        self.driver.close()

    # Test Case 1: Term and Condition Page
    def test_termsAndConditionsPage(self):
        homePage(self.driver).clickButton("Terms and Conditions")
        termsAndConditionsPage(self.driver).presentText("Definitions")
        termsAndConditionsPage(self.driver).presentText("Use License")
        termsAndConditionsPage(self.driver).presentText("Disclaimer")
        termsAndConditionsPage(self.driver).presentText("General Terms")

if __name__ == '__main__':
    unittest.main()