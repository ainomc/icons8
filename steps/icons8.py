# -*- coding: utf-8 -*-
from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, TimeoutException, StaleElementReferenceException
from datetime import datetime, timedelta
import selenium.webdriver.common.action_chains as AC
from selenium.webdriver.common.action_chains import ActionChains
import time
import os
from logic.actions import *
from logic.clickactions import *
from logic.locateactions import *
from logic.generators import *


TIME_FOR_WAIT = 30

Value_generate = ValueGenerate()
File_actions = FileActions()
Random_generate = RandomGenerate()



"""   ClickActions class___   """


# Then we have behave installed
@given('we have behave installed')
def step_impl(context):
    pass

@then("push link '{link}'")
# Then push link 'link text'
def step(context, link):
    context.clickActions = ClickActions(context)
    context.clickActions.click_on_link(link)

@then("try push link '{link}'")
# Then push link 'link text'
def step(context, link):
    context.clickActions = ClickActions(context)
    context.clickActions.try_click_on_link(link)

# Then button with text 'link text'
@then("button with text '{link}'")
def step(context, link):
    context.clickActions = ClickActions(context)
    context.clickActions.clickButtonText(link)

# Then click text 'text' [div]
@then("click text '{text}' [div]")
def step(context, text):
    context.clickActions = ClickActions(context)
    context.clickActions.click_text_with_div(text)

# Then click logo icon8
@then("click logo icon8")
def step(context):
    context.clickActions = ClickActions(context)
    context.clickActions.clickLogo()

# Then push link in navigation menu 'button'
@then("push link in navigation menu '{button}'")
def step(context, button):
    context.clickActions = ClickActions(context)
    context.clickActions.clickHeaderNavMenu(button)

# Then push second link 'link text'
@then("push second link '{link}'")
def step(context, link):
    xpath = "(//*[1][contains(text(), '%s')])[2]" % link
    context.clickActions = ClickActions(context)
    context.clickActions.click_on_xpath(xpath)
    
# Then push link in header 'link text'
@then("push link in header '{text_link}'")
def step(context, text_link):
    context.clickActions = ClickActions(context)
    context.clickActions.clickLogo()

# Then push 'button' from tabs
@then("push '{button}' from tabs")
def step(context, button):
    xpath = "//*[contains(text(), '%s')]" % button
    context.clickActions = ClickActions(context)
    context.clickActions.click_on_xpath(xpath)
   
# Then push link Logout
@then("push link Logout")
def step(context):
    xpath = "//*[@href='/logout/']"
    context.clickActions = ClickActions(context)
    context.clickActions.click_on_xpath(xpath)

# Then push link request icons
@then("push link Request icons")
def step(context):
    xpath = './/*[@href="/logout/"]'
    context.clickActions = ClickActions(context)
    context.clickActions.click_on_xpath(xpath)

# Then close popup
@then("close popup")
def step(context):
    xpath = "(//div[@class='ng-modal-close'])[last()]"
    context.clickActions = ClickActions(context)
    context.clickActions.click_on_xpath(xpath)
     
# Then push button 'button text'
@then("push button '{button}'")
def step(context, button):
    context.clickActions = ClickActions(context)
    context.clickActions.click_on_button(button)

# Then push unactive tab 'Collections'
@then("push unactive tab")
def step(context):
    tab = 'b-tab'
    context.clickActions = ClickActions(context)
    context.clickActions.click_on_unactive_tab(tab)

#Then push button 'Create'    
@then("Then push 'Create'")
def step(context):
    create = 'b-collection-preview-create'
    context.clickActions = ClickActions(context)
    context.clickActions.click_on_create(create)
     
# Then push button what named 'Name button text'
@then("push button what named '{name}'")
def step(context, name):
    context.clickActions = ClickActions(context)
    context.clickActions.click_on_button_findByName(name)

# Choose random style of request icon
# Then choose style of request icon
@then("choose style of request icon")
def step(context):
    xpath = '//*[@ng-repeat="platform in icCtrl.platforms"][%s]' % Random_generate.random_betweenValue(1,5)
    context.clickActions = ClickActions(context)
    context.clickActions.click_on_xpath(xpath)

# Clear similar ideas in Request icon pop-up
# Thaen clear similar ideas
@then("clear similar ideas")
def step(context):
    xpath = '//div[@ng-show="modal.template"]'
    context.clickActions = ClickActions(context)
    context.clickActions.click_on_xpath(xpath)

# Choose one type of ideas what alreade created by filter
# Then click '{filter}' filter of already created ideas
@then("click '{filter}' filter of already created ideas")
def step(context, filter):
    if filter == 'Hot ideas':
        xpath = '//*[@ng-repeat="filter in reqIcon.iconFilters"][1]'
    elif filter == 'Latest ideas':
        xpath = '//*[@ng-repeat="filter in reqIcon.iconFilters"][2]'
    elif filter == 'Popular ideas':
        xpath = '//*[@ng-repeat="filter in reqIcon.iconFilters"][3]'
    context.clickActions = ClickActions(context)
    context.clickActions.click_on_xpath(xpath)


# Choose click '{menu}' on request icon menu page
@then("click '{menu}' request icon menu")
def step(context, menu):
    if menu == 'Slow for Free':
        xpath = '//a[@ng-repeat="page in reqIcon.requestPages"][1]'
    #elif menu == 'Fast for $199/year':
        #xpath = '//a[@ng-repeat="page in reqIcon.requestPages"][2]'
    elif menu == 'Fastest for $50/icon':
        xpath = '//a[@ng-repeat="page in reqIcon.requestPages"][2]'
    context.clickActions = ClickActions(context)
    context.clickActions.click_on_xpath(xpath)

# Then click '{placeholder}' field
@then("click '{placeholder}' field")
def step(context, placeholder):
    xpath = '//*[@placeholder="%s"]' % placeholder
    context.clickActions = ClickActions(context)
    context.clickActions.click_on_xpath(xpath)

# Then click '{value}' element
@then("click '{value}' element")
def step(context, value):
    xpath = '//*[@value="%s"]' % value
    context.clickActions = ClickActions(context)
    context.clickActions.click_on_xpath(xpath)

# Then choose '{title}' element
@then("choose '{title}' element")
def step(context, title):
    xpath = '//*[@title="%s"]' % title
    context.clickActions = ClickActions(context)
    context.clickActions.click_on_xpath(xpath)

# Then click login button in register pop-up
@then("click login button in register pop-up")
def step(context):
    xpath = '//a[contains(., "Login")][@class]'
    context.clickActions = ClickActions(context)
    context.clickActions.click_on_xpath(xpath)

# Then click on filter '{number of filter}'
@then("click on filter '{num_of_filter}'")
def step(context, num_of_filter):
    xpath = './/*[@class="c-grid-btns"]/*[%s]' % num_of_filter
    context.clickActions = ClickActions(context)
    context.clickActions.click_on_xpath(xpath)

# Then click '{button}' button
@then("click '{button}' button")
def step(context, button):
    context.clickActions = ClickActions(context)
    context.clickActions.clickButton(button)

# Then try click '{button}' button
@then("try click '{button}' button")
def step(context, button):
    context.clickActions = ClickActions(context)
    context.clickActions.try_click_button(button)

# Then click buy '{type_of_buy}' button
@then("click buy '{type_of_buy}' button")
def step(context, type_of_buy):
    if type_of_buy == 'Free':
        move_to = '//div[@callback="goToWebApp()"]'
        button = """//div[@ng-bind-html="'PAGE.BUY.PLANS.FREE.GET' | translate"]"""
    elif type_of_buy == 'All 33,100 Icons':
        move_to = '//*[@callback="buyHoverBlock(licenses.companies.updates)"]'
        button = """//*[@ng-bind-html="'PAGE.BUY.PLANS.BUY' | translate"][@ng-class="licenses.companies.updates.id"]"""
    elif type_of_buy == 'Pay per Icon':
        Type_of_buy = Value_generate.values_in_range(2, 4)
        print (Type_of_buy)
        move_to = '//div[@register-modal-params="{registerTitle:registerTitle, loginTitle:loginTitle}"][%s]' % Type_of_buy
        button = '//div[@register-modal-params="{registerTitle:registerTitle, loginTitle:loginTitle}"][%s]/*[4]' % Type_of_buy
    context.clickActions = ClickActions(context)
    context.clickActions.moveAndClick(move_to, button)

# Then delete all '{elements}' elements
@then("delete all '{elements}' elements")
def step(context, elements):
    if elements == 'collections':
        xpathFirst = '//*[@ng-repeat="coll in vm.colls.colls" ][%s]/*[@ ng-show="collectionsEdit"]'
        xpathSecond = '//*[@class="c-btn modal__action-confirm modal__action"]'
    context.clickActions = ClickActions(context)
    context.clickActions.clickAllAndButtons(xpathFirst, xpathSecond)

# Then click '{ng_if_locator}' button element
@then("click '{ng_if_locator}' button element")
def step(context, ng_if_locator):
    context.clickActions = ClickActions(context)
    context.clickActions.clickFindByNg_if(ng_if_locator)

# Then choose 'link' download icon type in download pop-up
@then("choose '{link}' download icon type in download pop-up")
def step(context, link):
    context.clickActions = ClickActions(context)
    context.clickActions.click_download_icontype(link)

# Then choose 'link' dbutton in download pop-up
@then("choose '{link}' button in download pop-up")
def step(context, link):
    context.clickActions = ClickActions(context)
    context.clickActions.click_download_iconsize(link)

# Then click got it pop-up
@then("click got it pop-up")
def step(context):
    context.clickActions = ClickActions(context)
    context.clickActions.try_gotit()

# Then try push text '{text}'e
@then("try push text '{text}'")
def step(context, text):
    context.clickActions = ClickActions(context)
    context.clickActions.try_click_text(text)








    """   LocateActions class___   """

# Then locate image 'address'
@then("locate image '{link}'")
def step(context, link):
    xpath = "//img[@src='%s']" % link
    context.locateActions = LocateActions(context)
    context.locateActions.locate_element(xpath)


# Then locate category 'name'
@then("locate category '{name}'")
def step(context, name):
    xpath = "//a[@ng-href='%s']" % name
    context.locateActions = LocateActions(context)
    context.locateActions.locate_element(xpath)

# Then locate image 'text image'
@then("locate image text '{text_image}'")
def step(context, text_image):
     xpath = "//img[@alt='%s']" % text_image
     context.locateActions = LocateActions(context)
     context.locateActions.locate_element(xpath)

# Then locate text 'text'
@then("locate text '{text}'")
def step(context, text):
    context.locateActions = LocateActions(context)
    context.locateActions.locate_text(text)

# Then locate concrete text 'concrete_text'
@then("locate concrete text '{concrete_text}'")
def step(context, concrete_text):
    context.locateActions = LocateActions(context)
    context.locateActions.locate_concrete_text(concrete_text)

# Then pedro search
@then("pedro search")
def step(context):
    xpath = "//input[@placeholder='Find an icon']"
    context.locateActions = LocateActions(context)
    context.locateActions.locate_element(xpath)

# Then check locate '{element}' element
@then("check locate '{element}' element")
def step(context, element):
    context.locateActions = LocateActions(context)
    context.locateActions.locateElement(element)

# Then check ideas list in filter
@then("check ideas list in filter")
def step(context):
    xpath = '//*[@ng-model="idea"][%s]' % Value_generate.values_in_range(1, 5)
    context.locateActions = LocateActions(context)
    context.locateActions.locate_element(xpath)

# Then check recently created icons
@then("check recently created icons")
def step(context):
    xpath = '//a[@class="c-recently-icon"][%s]' % Value_generate.values_in_range(1, 5)
    context.locateActions = LocateActions(context)
    context.locateActions.locate_element(xpath)

# Then check ideas list
@then("check ideas list")
def step(context):
    xpath = '//div[@class="b-idea-table-row"][%s]' % Value_generate.values_in_range(1, 5)
    context.locateActions = LocateActions(context)
    context.locateActions.locate_element(xpath)

# Then locate search field
@then("locate search field")
def step(context):
     xpath = '//div[@class="b-col-1"]'
     context.locateActions = LocateActions(context)
     context.locateActions.locate_element(xpath)

# Then locate '{placeholder}' field
@then("locate '{placeholder}' field")
def step(context, placeholder):
    xpath = '//*[@placeholder="%s"]' % placeholder
    context.locateActions = LocateActions(context)
    context.locateActions.locate_element(xpath)

# Then find '{id}' element
@then("find '{id}' element")
def step(context, id):
    xpath = "//*[@id='%s']" % id
    context.locateActions = LocateActions(context)
    context.locateActions.locate_element(xpath)

# Then locate '{value}' element
@then("locate '{value}' element")
def step(context, value):
    xpath = '//*[@value="%s"]' % value
    context.locateActions = LocateActions(context)
    context.locateActions.locate_element(xpath)

# Then check last created idea
@then("check last created idea")
def step(context):
    pathToFile = os.path.join('steps', 'logic', 'ideas.txt')
    print (pathToFile + " - path to idea file")
    file_read_text = File_actions.read_file(pathToFile) #"steps\logic\ideas.txt"
    xpath = '//idea[1]/div/a[contains(., "%s")]' % file_read_text
    context.locateActions = LocateActions(context)
    assert context.locateActions.locate_element(xpath)

# Then absent '{element}' element
@then("absent '{element}' element")
def step(context, element):
    if element == 'search result':
        xpath = '//*[@single-icon="icon"]'
    context.locateActions = LocateActions(context)
    assert context.locateActions.absent_element(xpath)

# Then try find and check'{elements}'
@then("try find and check '{elements}'")
def step(context, elements):
    if elements == 'Unlock Font':
        try_find = '//*[1][contains(text(), "Unlock Font")]'
        click = '//*[1][contains(text(), "see pricing")]'
        find_second = '//*[1][contains(text(), "Paid or Free, You Are Our Hero!")]'
    elif elements == 'Color Icons Are Excluded':
        try_find = '//*[1][contains(text(), "Color Icons Are Excluded")]'
        click = '//a[1][contains(text(), "ok")]'
        find_second = '//*[@callback="downloadIconsCollection()"]'
    context.locateActions = LocateActions(context)
    context.locateActions.tryFindClickFind(try_find, click, find_second)

# Then locate '{element}' element in color pop-up
@then("locate '{element}' element in color pop-up")
def step(context, element):
    if element == 'grayscale' or element == 'color' or element == 'color' or element == 'color_palette' or element == 'custom':
        xpath = '''//*[@class="colors"]/*/*[@ng-bind-html="'WEB_APP.RECOLOR.%s' | translate"]''' % element.upper()
    elif element == 'gray colors':
        xpath = '//*[@class="colors"]/descendant::*[@ng-repeat="color_ in colorsGray"][%s]' % Value_generate.values_in_range(1, 5)
    elif element == 'not gray colors':
        xpath = '//*[@class="colors-block"][2]/*[%s]' % Value_generate.values_in_range(1, 10)
    elif element == 'canvas':
        xpath = '//*[@class="colors"]/descendant::*/canvas'
    context.locateActions = LocateActions(context)
    context.locateActions.locate_element(xpath)












    """   MovementActions class___   """

# Прокрутить вниз страницы
# Then scroll to end of the page
@then("scroll to end of the page")
def step(context):
    mvementActions = MovementActions(context)
    mvementActions.scroll_down()

# Прокрутить в вверх страницы
# Then scroll to begin of the page
@then("scroll to begin of the page")
def step(context):
    mvementActions = MovementActions(context)
    mvementActions.scroll_up()

# Then move mouse to '{element_to}' element
@then("move mouse to '{element_to}' element")
def step(context, element_to):
    mvementActions = MovementActions(context)
    mvementActions.move_mouse(element_to)












    """   ___TextActions class___   """


# Then add text to field
@then("add text to '{field}'")
def step(context, field):
    text = Random_generate.random_idea_name()
    context.textActions = TextActions(context)
    context.textActions.input_text(text, field)


# Then add '{input_text}' text to '{locator_field}' field
@then("add '{input_text}' text to '{locator_field}' field")
def step(context, input_text, locator_field):
    context.textActions = TextActions(context)
    context.textActions.addTextToField(input_text, locator_field)












    """   ___pageActions class___   """

# Then go to Main page
@then("go to Main page")
def step(context):
    context.pageActions = PageActions(context)
    context.pageActions.open_main_page()

# Then back to previous page
@then("back to previous page")
def step(context):
    context.pageActions = PageActions(context)
    context.pageActions.back_to_previous_page()

# Then login
@then("login")
def step(context):
    context.pageActions = PageActions(context)
    context.pageActions.login()

# Then try login
@then("try login")
def step(context):
    try:
        context.locateActions = LocateActions(context)
        context.pageActions = PageActions(context)
        context.clickActions = ClickActions(context)
        context.locateActions.locate_text('Login')
        context.locateActions.locate_text('Register')
        context.clickActions.click_on_link('click here')
        login_button = '//a[contains(., "Login")][@class]'
        context.clickActions.click_on_xpath(login_button)
        context.pageActions.login()
    except TimeoutException:
        pass













"""   ___Helpers class___   """

# Then sleep '{time}' seconds
@then("sleep '{time}' seconds")
def step(context, time):
    context.helpers = Helpers(context)
    context.helpers.sleepTime(time)

# Then check and delete '{file}' file
@then("check and delete '{file}' file")
def step(context, file):
    x = context
    File_actions.delete_file(file)

# Then check and delete '{extension}' file by extension
@then("check and delete '{extension}' file by extension")
def step(context, extension):
    x = context
    File_actions.del_by_extension(extension)


# Then wait downloading end of '{extension}' file
@then("wait downloading end of '{extension}' file")
def step(context, extension):
    x = context
    File_actions.downloading_file(extension)

