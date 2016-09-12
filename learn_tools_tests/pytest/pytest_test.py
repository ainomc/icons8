from selenium import webdriver
import pytest
# python -m pytest -v pytest_test.py -s

def setup_module(module):
    module.driver = webdriver.Firefox()
    module.driver.get("https://demo.icons8.com")

def teardown_module(module):
    module.driver.close()

class Test:

    def test_termsAndConditionsPage(self):
        homePage(self).clickButton("Terms and Conditions")
        termsAndConditionsPage(self).presentText("Definitions")
        #termsAndConditionsPage(driver).presentText("Use License")
        #termsAndConditionsPage(driver).presentText("Disclaimer")
        #termsAndConditionsPage(driver).presentText("General Terms")

# Logic on Home Page
class homePage(object):

    def __init__(self, driver):
        self.driver = driver

    # click button by xpath and contains text
    def clickButton(self, button):
        self.driver.find_element_by_xpath('//*[1][contains(text(), "%s")]' % button).click()
        return True

# Logic on Term and Condition Page
class termsAndConditionsPage(object):

    def __init__(self, driver):
        self.driver = driver

    # check presents of text by xpath and contains text
    def presentText(self, text):
        self.driver.find_element_by_xpath('//*[contains(text(), "%s")]' % text)
        return True



"""
class TestRegisterNewInstructor:

    def setup_class(pytest):
        pytest.driver = webdriver.Firefox()
        pytest.driver.get("https://demo.icons8.com")

    def test_01_LoginWithAdmin(self):
        print ("xXx")

    def teardown_class(pytest):
        pytest.driver.close()

"""





# python -m pytest --driver Firefox pytest_test.py


"""
def setup_module(module):
    driver.get('https://demo.icons8.com')
    driver.implicitly_wait(10)
    print ("setup_module      module:%s" % module.__name__)

def teardown_module(module):
    driver = webdriver
    driver.close()
    print ("teardown_module   module:%s" % module.__name__)

def setup_function(function):
    driver.get("https://demo.icons8.com")
    print ("setup_function    function:%s" % function.__name__)

def teardown_function(function):
    driver.get("https://demo.icons8.com")
    print ("teardown_function function:%s" % function.__name__)

def test_termsAndConditionsPage():
    homePage(driver).clickButton("Terms and Conditions")
    termsAndConditionsPage(driver).presentText("Definitions")
    termsAndConditionsPage(driver).presentText("Use License")
    termsAndConditionsPage(driver).presentText("Disclaimer")
    termsAndConditionsPage(driver).presentText("General Terms")

class Test:
    def setup(self):
            driver.get("https://demo.icons8.com")
            print ("setup             class:TestStuff")

    def teardown(self):
            driver.get("https://demo.icons8.com")
            print ("teardown          class:TestStuff")


    # Test Case 1: Term and Condition Page
    def test_termsAndConditionsPage(self):
        homePage(driver).clickButton("Terms and Conditions")
        termsAndConditionsPage(driver).presentText("Definitions")
        termsAndConditionsPage(driver).presentText("Use License")
        termsAndConditionsPage(driver).presentText("Disclaimer")
        termsAndConditionsPage(driver).presentText("General Terms")

# Logic on Home Page
class homePage:

    def __init__(self, driver):
        driver = driver
    # click button by xpath and contains text
    def clickButton(self, button):
        driver.find_element_by_xpath('//*[1][contains(text(), "%s")]' % button).click()
        return True



# Logic on Term and Condition Page
class termsAndConditionsPage:

    # Logic before test
    def __init__(self, driver):
        driver = driver

    # check presents of text by xpath and contains text
    def presentText(self, text):
        driver.find_element_by_xpath('//*[contains(text(), "%s")]' % text)
        return True



# python -m pytest -v pytest_test.py

def ssetup_module(module):
    self.driver = webdriver.Firefox()
    self.driver.get("https://demo.icons8.com")
    self.driver.implicitly_wait(10)
    print ("Test start")


# Logic after test
    def teardown_module(module):
        print ("Test end")
        self.driver.close()



# Logic on Home Page
class homePage(object):

    def __init__(self, driver):
        self.driver = driver
    # click button by xpath and contains text
    def clickButton(self, button):
        self.driver.find_element_by_xpath('//*[1][contains(text(), "%s")]' % button).click()
        return True



# Logic on Term and Condition Page
class termsAndConditionsPage(object):

    # Logic before test
    def __init__(self, driver):
        self.driver = driver

    # check presents of text by xpath and contains text
    def presentText(self, text):
        self.driver.find_element_by_xpath('//*[contains(text(), "%s")]' % text)
        return True

# Test Cases
class TestCases:
    def setup(self):
        self.driver.get("https://demo.icons8.com")
        print ("Test start")

    def teardown(self):
        self.driver.get("https://demo.icons8.com")
        print ("Test end")

    # Test Case 1: Term and Condition Page
    def test_termsAndConditionsPage(self):
        homePage(self.driver).clickButton("Terms and Conditions")
        termsAndConditionsPage(self.driver).presentText("Definitions")
        termsAndConditionsPage(self.driver).presentText("Use License")
        termsAndConditionsPage(self.driver).presentText("Disclaimer")
        termsAndConditionsPage(self.driver).presentText("General Terms")
"""

