# -*- coding: utf-8 -*-
"""Locators for tests"""

from generators import ValueGenerate
Value_generate = ValueGenerate()

locators_dict = {
'icons result': '//div[@class="b-subcategory-wrapper"][1]/descendant::a[%s]'
                            % Value_generate.values_in_range(1, 5),
'icons in result': '//div[@class="b-subcategory-wrapper"][1]/descendant::a[%s]'
                   % Value_generate.values_in_range(1, 3),
'first icon in collection': './/*[@class="icons-set m-firefox"]/'
                            'div[@draggable-type="fromLightBox"][1]',
'created first collection': '//*[@class="b-collections-container"]/div[1]',
'created second collection': '//*[@class="b-collections-container"]/div[2]',
'Get Font pop-up': '//*[@stop-events="click"]',
'Public Link': '//*[@ng-model="colSharing.url"]',
'icon category': '//*[@class="c-breadcrumbs"]/*[%s]'
                     % Value_generate.values_in_range(1, 3),
'icon text': './/*[@ng-bind-html="vm.mainSubtitleText"]',
'Icon': '//*[@class="col-md-4 m-full-width b-main-icon m-main-icon"]/*',
'Download button': '//button[contains(text(), "Download")]',
'icon download sizes': '//ul[@class="c-list m-nooverflow"]/*[%s]'
                           % Value_generate.values_in_range(1, 4),
'icon download format': '//*[@class="c-list m-nooverflow b-format"]/*[%s]'
                            % Value_generate.values_in_range(1, 6),
'Category Title': '//*[@ng-bind-html="vm.category.title"]',
'simple list': './/*[@class="c-icon-list"]',
'list with names': './/*[@class="c-icon-list m-with-name"]',
'table list': '''.//*[@ng-if="vm.gridState.state == 'table'"]''',


'search': '//*[@class="b-search-btn"]',
'search platform filter': './/*[@class="b-bar-menus m-fix-c-list"]/*[1]/*[%s]'
                              % Value_generate.values_in_range(2, 8),
'first icon in result': '//div[@class="b-subcategory-wrapper"][1]/descendant::a[1]',
'search category': './/*[@class="b-bar-menus-menu m-scrollable"]/descendant::a[%s]'
                       % Value_generate.values_in_range(3, 50),
'new icons search category':
        './/*[@class="b-bar-menus-menu m-scrollable"]/descendant::*[@class="c-list m-padding b-bar-menus-menu"][2]/a[1]',
'Paypal': '''.//*[@id='page-app']/modals/descendant::*[@class="b-payment-description"]''',
'Credit cards': '''.//*[@id='page-app']/modals/descendant::*[@class="b-payment-svg xxxx"]''',
'Download for Windows': '//*[@click-need-register="//icons8.com/downloader/?pack=appWin"]',
'Collections': '//span[contains(., "Collections")]',
'Create collections': './/*[@ng-click="vm.createCollection();"]',
'confirm name': './/*[@ng-if="vm.collectionRenaming"]/*[@ng-click="vm.renameCollection()"]/*',
'delete collection menu': '''.//*[@ng-class="{'m-edit': collectionsEdit}"]''',
'delete icon in collection': '//span[@class="c-btn m-transparent"]',
'Get Font': '''//*[@popup-target="'generate-font'"]''',
'Get SVG Set': '''.//*[@class="b-bar-btns m-collections"]/div[3]''',
'open public link pop-up': '//*[@class="c-tooltip m-no-border m-share-link-tooltip"]',
'color palette': '//*[@class="colors"]/descendant::*[@ng-class="{active: showPicker}"]',
'open color pop-up': '//*[@hide-color-picker="hideColorPicker"]/*[@ng-if="!hideColorPicker"]',
'recommend': '//*[@class="infinario-block__poll"]/*[%s]' % Value_generate.values_in_range(1, 11),
'icon name': '//*[@class="c-pretty-link m-inline"]',
'tag': '//*[@class="b-tags-list"]/a[1]',
'icon in tag page': '//span[@class="icons-set_element"][1]',
'choose size of PNG': '//*[@class="icon-format-item icon-format-dropdown off-click-dropdownsize m-center"]',
'Download for Windows': "//*[@id='home-app']/div[1]/div[2]/div/div/div[1]/div/a",
'Download in icon bar': './/*[@class="b-bar-btns m-icon"]/*[1]',
'Download in icon bar esp': './/*[@class="b-bar-btns m-icon m-single-btn"]/*[1]',
'Open download icon pop-up': './/*[@class="icon-format-item icon-format-dropdown off-click-dropdownsize m-center"]',
'Edit name': './/div[@i8-simple-tooltip="Edit name"]',
'Got it': './/div[@class="c-btn b-message-button"]',
'Profile': '//a[contains(text(), "Profile")][1]',
'API': '//a[contains(text(), "API")][1]',
'delete icon': '//div[@class="c-btn modal__action-confirm modal__action"]',
'Unlimited Plan buy': './/*[@class="b-license m-order-0"]/descendant::*[@class="c-btn m-pricing ng-binding ng-isolate-scope"]',
'Free buy': './/*[@class="b-license m-order-1"]/descendant::*[@class="c-btn m-pricing ng-binding ng-isolate-scope"]',
'Service Integration buy': './/*[@class="b-license m-order-2"]/descendant::*[@class="c-btn m-pricing ng-binding ng-isolate-scope"]',
'icon8 app in download pop-up': './/*[@class="c-big-menu c-big-menu-narrow active"]/descendant::*[@href="/app"]',
'Download menu': './/*[@for="big-menu-download"]'
}
