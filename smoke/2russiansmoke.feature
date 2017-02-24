Feature: Open pages, login and assertions
Scenario: Choose russian localisation
Scenario: 1: Choose russian localisation
  Then click logo icon8
  Then click 'selectLanguage' button element
  Then click text 'Russian' [div]

Scenario: Terms and Conditions
Scenario: 2: Open Terms and Conditions page (Пользовательское соглашение) and assert text
  Then click logo icon8
  Then push link 'Пользовательское'
  Then scroll to end of the page
  Then locate text 'Наша бизнес-модель'
  Then locate text 'Бесплатная лицензия'
  Then locate text 'Купить полную лицензию'
  Then locate text 'Версия для большого экрана'
  Then click logo icon8

Scenario: Privacy Policy
Scenario: 3: Open Privacy Policy (Конфиденциальность) page and assertion
  Then click logo icon8
  Then push link 'Конфиденциальность'
  Then scroll to end of the page
  Then locate text 'Наша бизнес-модель'
  Then locate text 'Бесплатная лицензия'
  Then locate text 'Купить полную лицензию'
  Then locate text 'Версия для большого экрана'
  Then click logo icon8

Scenario: Free license
Scenario: 4: Open Free license page (Бесплатные иконки) and assertion
  Then click logo icon8
  Then push link 'Бесплатные иконки'
  Then scroll to end of the page
  Then locate text 'Иконки — бесплатно'
  Then locate text 'Зачем ставить ссылку?'
  Then locate text 'Где ставить ссылку?'
  Then locate text 'Веб-сайты'
  Then locate text 'Приложения для компьютеров'
  Then locate text 'Мобильные приложения'
  Then locate text 'Open Source'
  Then click logo icon8

Scenario: Paid license
Scenario: 5: Open Paid license page (Платные иконки) and assertion
  Then click logo icon8
  Then push link 'Платные иконки'
  Then scroll to end of the page
  Then locate text 'За деньги или бесплатно'
  Then locate text 'Платная лицензия вкратце'
  Then locate text 'Запрещено для всех лицензий'
  Then locate text 'Что включено'
  Then locate text 'Возможности редактора иконок'
  Then locate text 'Приложение для Мака и Windows'
  Then locate image '//cdnd.icons8.com/download/images/features_video_27.02.png'
  Then click logo icon8

Scenario: Contact us
Scenario: 6: Open Contact us (Напишите нам) page and assertion
  Then click logo icon8
  Then push link 'Напишите нам'
  Then scroll to end of the page
  Then locate text 'Contact Icons8'
  Then locate text 'Talk to a Human'
  Then locate text 'Our support team consists'
  Then click logo icon8

Scenario: Apps Win / Mac
Scenario: 7: Open Application page and assertion
  Then click logo icon8
  Then push link 'Скачать'
  Then click 'icon8 app in download pop-up' button
  Then scroll to end of the page
  Then locate text 'Скачать все иконки в одном приложении'
  Then locate text 'Скачать для'
  Then locate text 'Другие варианты загрузки'
  Then locate text 'Boзмoжнocти'
  Then locate text 'Все иконки, которые потребуются'
  Then locate text 'Самые популярные'
  Then locate text 'Посмотреть все'
  Then locate text 'Возможности для дизайнеров'
  Then locate text 'В одном стиле'
  Then locate text 'Редактируемые'
  Then locate text 'Перекрашивание иконки'
  Then locate text 'Ежедневные обновления'
  Then locate text '«Я люблю Icons8»'
  Then click logo icon8

Scenario: Request icons
Scenario: 8: Open Request icons (Попросить) page and assertion
  Then click logo icon8
  Then push link 'Попросить'
  Then scroll to end of the page
  Then locate text 'Попросить нарисовать'
  Then locate text 'Горячие идеи'
  Then locate text 'Свежие идеи'
  Then locate text 'Популярные идеи'
  Then locate text 'Посмотреть все идеи для иконок'
  Then locate text 'Недавно созданные иконки'
  Then push 'Молниеносно по 50$' from tabs
  Then locate text 'Как быстро?'
  Then locate text 'Сколько это стоит?'
  Then locate text 'С чего начать?'
  Then push 'Несрочно бесплатно' from tabs
  Then locate text 'Недавно созданные иконки'
  Then click logo icon8

Scenario: Cosmic Pedro
Scenario: 9: Open Cosmic Pedro page and assertion
  Then click logo icon8
  Then button with text 'Labs'
  Then push link 'Cosmic Pedro'
  Then locate text 'Cosmic Pedro'
  Then locate text 'Search for icon. Add text. Share!'
  Then go to Main page

Scenario: We love SVG
Scenario: 10: Open We love SVG page and assertion
  Then click logo icon8
  Then button with text 'Labs'
  Then push link 'We Love SVG'
  Then scroll to end of the page
  Then locate text 'Flat Color'
  Then push link 'Hello World!'
  Then locate text 'Simple jQuery Example'
  Then locate text '!DOCTYPE html'
  Then close popup
  Then back to previous page
  Then click logo icon8

Scenario: Web app
Scenario: 11: Open Web app page and assertion
  Then click logo icon8
  Then click 'selectLanguage' button element
  Then click text 'Russian' [div]
  Then click logo icon8
  Then push link 'Иконки'
  Then scroll to end of the page
  Then locate text 'Новые иконки'
  Then locate text 'Скачать'
  Then locate text 'Сделать HTML'
  Then locate text 'Иконка'
  Then click logo icon8

Scenario: Logout feature
Scenario: 12: Logout and assertion
  Then click logo icon8
  Then locate text 'Личный кабинет'
  Then push link Logout
  Then push link 'Вход'
  Then locate text 'Вход в Icons8'
  Then locate text 'Забыли пароль?'
  Then push link 'Регистрация'
