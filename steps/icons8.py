# -*- coding: utf-8 -*-
"""Convert Gherkin to the real code what run some actions"""
from behave import *
from logic.clickactions import *
from logic.locateactions import *
from logic.generators import ValueGenerate, FileActions, RandomGenerate
from logic.actions import PageActions, TextActions, MovementActions, Helpers
from selenium.common.exceptions import TimeoutException

# init
Value_generate = ValueGenerate()
File_actions = FileActions()
Random_generate = RandomGenerate()


"""   ClickActions class___   """


@given('we have behave installed')
def step_impl(context):
    """Then we have behave installed"""
    pass

@then("push link '{link}'")
def step(context, link):
    """Then push link 'link text'"""
    context.clickActions = ClickActions(context)
    context.clickActions.click_on_link(link)

@then("try push link '{link}'")
def step(context, link):
    """Then push link 'link text'"""
    context.clickActions = ClickActions(context)
    context.clickActions.try_click_on_link(link)

@then("button with text '{link}'")
def step(context, link):
    """Then button with text 'link text'"""
    context.clickActions = ClickActions(context)
    context.clickActions.clickButtonText(link)

@then("click text '{text}' [div]")
def step(context, text):
    """Then click text 'text' [div]"""
    context.clickActions = ClickActions(context)
    context.clickActions.click_text_with_div(text)

@then("click logo icon8")
def step(context):
    """Then click logo icon8"""
    context.clickActions = ClickActions(context)
    context.clickActions.clickLogo()

@then("push link in navigation menu '{button}'")
def step(context, button):
    """Then push link in navigation menu 'button'"""
    context.clickActions = ClickActions(context)
    context.clickActions.clickHeaderNavMenu(button)

@then("push second link '{link}'")
def step(context, link):
    """Then push second link 'link text'"""
    xpath = "(//*[1][contains(text(), '%s')])[2]" % link
    context.clickActions = ClickActions(context)
    context.clickActions.click_on_xpath(xpath)
    
@then("push link in header '{text_link}'")
def step(context, text_link):
    """Then push link in header 'link text'"""
    context.clickActions = ClickActions(context)
    context.clickActions.clickLogo()

@then("push '{button}' from tabs")
def step(context, button):
    """Then push 'button' from tabs"""
    xpath = "//*[contains(text(), '%s')]" % button
    context.clickActions = ClickActions(context)
    context.clickActions.click_on_xpath(xpath)
   
@then("push link Logout")
def step(context):
    """Then push link Logout"""
    xpath = "//*[@href='/logout/']"
    time.sleep(2)
    context.clickActions = ClickActions(context)
    context.clickActions.click_on_xpath(xpath)
    time.sleep(2)

@then("push link Request icons")
def step(context):
    """Then push link request icons"""
    xpath = './/*[@href="/logout/"]'
    context.clickActions = ClickActions(context)
    context.clickActions.click_on_xpath(xpath)

@then("close popup")
def step(context):
    """Then close popup"""
    xpath = "(//div[@class='ng-modal-close'])[last()]"
    context.clickActions = ClickActions(context)
    context.clickActions.click_on_xpath(xpath)

@then("push button '{button}'")
def step(context, button):
    """Then push button 'button text'"""
    context.clickActions = ClickActions(context)
    context.clickActions.click_on_button(button)

@then("push unactive tab")
def step(context):
    """ Then push unactive tab 'Collections'"""
    tab = 'b-tab'
    context.clickActions = ClickActions(context)
    context.clickActions.click_on_unactive_tab(tab)

@then("Then push 'Create'")
def step(context):
    """Then push button 'Create' """
    create = 'b-collection-preview-create'
    context.clickActions = ClickActions(context)
    context.clickActions.click_on_create(create)
     
@then("push button what named '{name}'")
def step(context, name):
    """Then push button what named 'Name button text'"""
    context.clickActions = ClickActions(context)
    context.clickActions.click_on_button_findByName(name)

@then("choose style of request icon")
def step(context):
    """Choose random style of request icon
    Then choose style of request icon
    """
    xpath = '//*[@ng-repeat="platform in icCtrl.platforms"][%s]' % Random_generate.random_betweenValue(1,5)
    context.clickActions = ClickActions(context)
    context.clickActions.click_on_xpath(xpath)

@then("clear similar ideas")
def step(context):
    """Clear similar ideas in Request icon pop-up
    Than clear similar ideas
    """
    xpath = '//div[@ng-show="modal.template"]'
    context.clickActions = ClickActions(context)
    context.clickActions.click_on_xpath(xpath)

@then("click '{filter}' filter of already created ideas")
def step(context, filter):
    """Choose one type of ideas what already created by filter
    Then click '{filter}' filter of already created ideas
    """
    if filter == 'Hot ideas':
        xpath = '//*[@ng-repeat="filter in reqIcon.iconFilters"][1]'
    elif filter == 'Latest ideas':
        xpath = '//*[@ng-repeat="filter in reqIcon.iconFilters"][2]'
    elif filter == 'Popular ideas':
        xpath = '//*[@ng-repeat="filter in reqIcon.iconFilters"][3]'
    context.clickActions = ClickActions(context)
    context.clickActions.click_on_xpath(xpath)


@then("click '{menu}' request icon menu")
def step(context, menu):
    """Choose click '{menu}' on request icon menu page"""
    if menu == 'Slow for Free':
        xpath = '//a[@ng-repeat="page in reqIcon.requestPages"][1]'
    elif menu == 'Fastest for $50/icon':
        xpath = '//a[@ng-repeat="page in reqIcon.requestPages"][2]'
    context.clickActions = ClickActions(context)
    context.clickActions.click_on_xpath(xpath)

@then("click '{placeholder}' field")
def step(context, placeholder):
    """Then click '{placeholder}' field"""
    xpath = '//*[@placeholder="%s"]' % placeholder
    context.clickActions = ClickActions(context)
    context.clickActions.click_on_xpath(xpath)

@then("click '{value}' element")
def step(context, value):
    """Then click '{value}' element"""
    xpath = '//*[@value="%s"]' % value
    context.clickActions = ClickActions(context)
    context.clickActions.click_on_xpath(xpath)

@then("choose '{title}' element")
def step(context, title):
    """Then choose '{title}' element"""
    xpath = '//*[@title="%s"]' % title
    context.clickActions = ClickActions(context)
    context.clickActions.click_on_xpath(xpath)

@then("click login button in register pop-up")
def step(context):
    """Then click login button in register pop-up"""
    xpath = '//a[contains(., "Login")][@class]'
    context.clickActions = ClickActions(context)
    context.clickActions.click_on_xpath(xpath)

@then("click on filter '{num_of_filter}'")
def step(context, num_of_filter):
    """Then click on filter '{number of filter}'"""
    xpath = './/*[@class="c-grid-btns"]/*[%s]' % num_of_filter
    context.clickActions = ClickActions(context)
    context.clickActions.click_on_xpath(xpath)

@then("click '{button}' button")
def step(context, button):
    """Then click '{button}' button"""
    context.clickActions = ClickActions(context)
    context.clickActions.clickButton(button)

@then("try click '{button}' button")
def step(context, button):
    """Then try click '{button}' button"""
    context.clickActions = ClickActions(context)
    context.clickActions.try_click_button(button)

@then("click buy '{type_of_buy}' button")
def step(context, type_of_buy):
    """Then click buy '{type_of_buy}' button"""
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

@then("delete all '{elements}' elements")
def step(context, elements):
    """Then delete all '{elements}' elements"""
    if elements == 'collections':
        xpathFirst = '//*[@ng-repeat="coll in vm.colls.colls" ][%s]/*[@ ng-show="collectionsEdit"]'
        xpathSecond = '//*[@class="c-btn modal__action-confirm modal__action"]'
    context.clickActions = ClickActions(context)
    context.clickActions.clickAllAndButtons(xpathFirst, xpathSecond)

@then("click '{ng_if_locator}' button element")
def step(context, ng_if_locator):
    """Then click '{ng_if_locator}' button element"""
    context.clickActions = ClickActions(context)
    context.clickActions.clickFindByNg_if(ng_if_locator)

@then("choose '{link}' download icon type in download pop-up")
def step(context, link):
    """Then choose 'link' download icon type in download pop-up"""
    context.clickActions = ClickActions(context)
    context.clickActions.click_download_icontype(link)

@then("choose '{link}' button in download pop-up")
def step(context, link):
    """Then choose 'link' dbutton in download pop-up"""
    context.clickActions = ClickActions(context)
    context.clickActions.click_download_iconsize(link)

@then("click got it pop-up")
def step(context):
    """Then click got it pop-up"""
    context.clickActions = ClickActions(context)
    context.clickActions.try_gotit()

@then("try push text '{text}'")
def step(context, text):
    """Then try push text '{text}'"""
    context.clickActions = ClickActions(context)
    context.clickActions.try_click_text(text)


    """   LocateActions class___   """

@then("locate image '{link}'")
def step(context, link):
    """Then locate image 'address'"""
    xpath = "//img[@src='%s']" % link
    context.locateActions = LocateActions(context)
    context.locateActions.locate_element(xpath)

@then("locate category '{name}'")
def step(context, name):
    """Then locate category 'name'"""
    xpath = "//a[@ng-href='%s']" % name
    context.locateActions = LocateActions(context)
    context.locateActions.locate_element(xpath)

@then("locate image text '{text_image}'")
def step(context, text_image):
    """Then locate image 'text image'"""
    xpath = "//img[@alt='%s']" % text_image
    context.locateActions = LocateActions(context)
    context.locateActions.locate_element(xpath)

@then("locate text '{text}'")
def step(context, text):
    """Then locate text 'text'"""
    context.locateActions = LocateActions(context)
    context.locateActions.locate_text(text)

@then("locate concrete text '{concrete_text}'")
def step(context, concrete_text):
    """Then locate concrete text 'concrete_text'"""
    context.locateActions = LocateActions(context)
    context.locateActions.locate_concrete_text(concrete_text)

@then("pedro search")
def step(context):
    """Then pedro search"""
    xpath = "//input[@placeholder='Find an icon']"
    context.locateActions = LocateActions(context)
    context.locateActions.locate_element(xpath)

@then("check locate '{element}' element")
def step(context, element):
    """Then check locate '{element}' element"""
    context.locateActions = LocateActions(context)
    context.locateActions.locateElement(element)

@then("check ideas list in filter")
def step(context):
    """Then check ideas list in filter"""
    xpath = '//*[@ng-model="idea"][%s]' % Value_generate.values_in_range(1, 5)
    context.locateActions = LocateActions(context)
    context.locateActions.locate_element(xpath)

@then("check recently created icons")
def step(context):
    """Then check recently created icons"""
    xpath = '//a[@class="c-recently-icon"][%s]' % Value_generate.values_in_range(1, 5)
    context.locateActions = LocateActions(context)
    context.locateActions.locate_element(xpath)

@then("check ideas list")
def step(context):
    """Then check ideas list"""
    xpath = '//div[@class="b-idea-table-row"][%s]' % Value_generate.values_in_range(1, 5)
    context.locateActions = LocateActions(context)
    context.locateActions.locate_element(xpath)

@then("locate search field")
def step(context):
    """Then locate search field"""
    xpath = '//div[@class="b-col-1"]'
    context.locateActions = LocateActions(context)
    context.locateActions.locate_element(xpath)

@then("locate '{placeholder}' field")
def step(context, placeholder):
    """Then locate '{placeholder}' field"""
    xpath = '//*[@placeholder="%s"]' % placeholder
    context.locateActions = LocateActions(context)
    context.locateActions.locate_element(xpath)

@then("find '{id}' element")
def step(context, id):
    """Then find '{id}' element"""
    xpath = "//*[@id='%s']" % id
    context.locateActions = LocateActions(context)
    context.locateActions.locate_element(xpath)

@then("locate '{value}' element")
def step(context, value):
    """Then locate '{value}' element"""
    xpath = '//*[@value="%s"]' % value
    context.locateActions = LocateActions(context)
    context.locateActions.locate_element(xpath)

@then("check last created idea")
def step(context):
    """Then check last created idea"""
    pathToFile = os.path.join('steps', 'logic', 'ideas.txt')
    print (pathToFile + " - path to idea file")
    file_read_text = File_actions.read_file(pathToFile) #"steps\logic\ideas.txt"
    xpath = '//idea[1]/div/a[contains(., "%s")]' % file_read_text
    context.locateActions = LocateActions(context)
    assert context.locateActions.locate_element(xpath)

@then("absent '{element}' element")
def step(context, element):
    """Then absent '{element}' element"""
    if element == 'search result':
        xpath = '//*[@single-icon="icon"]'
    context.locateActions = LocateActions(context)
    assert context.locateActions.absent_element(xpath)

@then("try find and check '{elements}'")
def step(context, elements):
    """Then try find and check'{elements}'"""
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

@then("locate '{element}' element in color pop-up")
def step(context, element):
    """Then locate '{element}' element in color pop-up"""
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


@then("scroll to end of the page")
def step(context):
    """Then scroll to end of the page"""
    mvementActions = MovementActions(context)
    mvementActions.scroll_down()

@then("scroll to begin of the page")
def step(context):
    """Then scroll to begin of the page"""
    mvementActions = MovementActions(context)
    mvementActions.scroll_up()

@then("move mouse to '{element_to}' element")
def step(context, element_to):
    """Then move mouse to '{element_to}' element"""
    mvementActions = MovementActions(context)
    mvementActions.move_mouse(element_to)



    """   ___TextActions class___   """


@then("add text to '{field}'")
def step(context, field):
    """Then add text to field"""
    text = Random_generate.random_idea_name()
    context.textActions = TextActions(context)
    context.textActions.input_text(text, field)


@then("add '{input_text}' text to '{locator_field}' field")
def step(context, input_text, locator_field):
    """Then add '{input_text}' text to '{locator_field}' field"""
    context.textActions = TextActions(context)
    context.textActions.addTextToField(input_text, locator_field)












    """   ___pageActions class___   """

# Then go to Main page
@then("go to Main page")
def step(context):
    """"""
    context.pageActions = PageActions(context)
    context.pageActions.open_main_page()

# Then back to previous page
@then("back to previous page")
def step(context):
    """"""
    context.pageActions = PageActions(context)
    context.pageActions.back_to_previous_page()

# Then login
@then("login")
def step(context):
    """"""
    context.pageActions = PageActions(context)
    context.pageActions.login()

# Then try login
@then("try login")
def step(context):
    """"""
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

# Then wait start download of '{extension}' file
@then("wait start download of '{extension}' file")
def step(context, extension):
    x = context
    File_actions.wait_presents_file(extension)

# Then wait '{extension}' file
@then("wait '{extension}' file")
def step(context, extension):
    x = context
    File_actions.wait_presents_file(extension)

