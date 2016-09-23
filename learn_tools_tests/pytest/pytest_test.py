from selenium import webdriver
import pytest
# python -m pytest -v pytest_test.py -s

class Page(object):
    def __init__(self, driver):
        self.driver = driver

class TestUM:
    def setup(self):
        self.driver.get("https://demo.icons8.com")

    def teardown(self):
        self.driver.get("https://demo.icons8.com")

    def setup_class(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.get("https://demo.icons8.com")

    def teardown_class(cls):
        cls.driver.close()

    def test_termsAndConditionsPage(self):
        homepage = homePage(self.driver)
        terms_conditionsPage = termsAndConditionsPage(self.driver)
        homepage.clickButton("Terms and Conditions")
        terms_conditionsPage.presentText("Definitions")
        terms_conditionsPage.presentText("Use License")
        terms_conditionsPage.presentText("Disclaimer")
        terms_conditionsPage.presentText("General Terms")

class homePage(Page):

    # click button by xpath and contains text
    def clickButton(self, button):
        self.driver.find_element_by_xpath('//*[1][contains(text(), "%s")]' % button).click()
        return True

class termsAndConditionsPage(Page):

    # check presents of text by xpath and contains text
    def presentText(self, text):
        self.driver.find_element_by_xpath('//*[contains(text(), "%s")]' % text)
        return True
