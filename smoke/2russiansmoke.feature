Feature: Open pages, login and assertions

Scenario: Choose russian localisation
Scenario: 1: Choose russian localisation
  Then click logo icon8
  Then click 'selectLanguage' button element
  Then push link 'Russian'
  Then locate text ' 33,200 бесплатных иконок'

Scenario: Terms and Conditions
Scenario: 2: Open Terms and Conditions page (Пользовательское соглашение) and assert text
  Then click logo icon8
  Then push link 'Пользовательское'
  Then scroll to end of the page
  #Then locate text 'Disclaimer'
  #Then locate text 'General Terms'
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
  #Then locate text 'Information We Collect'
  #Then locate text 'Opt-Out'
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
  Then locate text 'Все 33,200 иконок'
  Then locate text 'Платная лицензия вкратце'
  Then locate text 'Запрещено для всех лицензий'
  Then locate text 'Что включено'
  Then locate text 'Возможности редактора иконок'
  Then locate text 'Приложение для Мака и Windows'
  Then locate image '//cdnd.icons8.com/download/images/features_video_27.02.png'
  Then push 'Расширенная API' from tabs
  Then locate text 'Как юзать Api'
  Then locate text 'Расширенная лицензия двух словах'
  Then locate text 'Атрибуция'
  Then push 'Студенческая' from tabs
  Then locate text 'Мы раздаем иконки '
  Then locate text 'Что получают студенты'
  Then locate image '//cdnd.icons8.com/download/images/features_video_27.02.png'
  Then push 'Стандартная' from tabs
  Then locate text 'За деньги или бесплатно'
  Then click logo icon8

Scenario: Contact us
Scenario: 6: Open Contact us (Напишите нам) page and assertion
  Then click logo icon8
  Then push link 'Напишите нам'
  Then scroll to end of the page
  #Then locate text 'Contact Icons8'
  #Then locate text 'Talk to a Human'
  #Then locate text 'Our support team responds'
  #Then locate text 'Check'
  #Then locate text 'Can I use'
  #Then locate text 'Where do I'
  #Then locate text 'Which license'
  #Then locate text 'Other Questions'
  Then click logo icon8

Scenario: Apps Win / Mac
Scenario: 7: Open Application page and assertion
  Then click logo icon8
  Then push link 'Скачать'
  Then scroll to end of the page
  Then locate text 'Скачать все иконки в одном приложении'
  Then locate text 'Скачать для'
  Then locate text 'для Mac'
  Then locate text 'Обычный ZIP-файл'
  Then locate text 'Boзмoжнocти'
  Then locate text 'Как это работает'
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
  Then push 'Быстро за 199$' from tabs
  Then locate text 'Как быстро?'
  Then locate text 'Ограничения'
  Then locate text 'Подходит для заказа'
  Then locate text 'Не подходит для заказа'
  Then push 'Молниеносно по 50$' from tabs
  Then locate text 'Как быстро?'
  Then locate text 'Сколько это стоит?'
  Then locate text 'С чего начать?'
  Then push 'Несрочно бесплатно' from tabs
  Then locate text 'Недавно созданные иконки'
  Then click logo icon8

#Scenario: Cosmic Pedro
#Scenario: 9: Open Cosmic Pedro page and assertion
  #Then button with text 'Icons8'
  #Then push link 'Спецпроекты'
  #Then locate text 'Бесплатно'
  #Then button with text 'Бесплатно'
  #Then locate text 'Cosmic Pedro'
  #Then locate text 'Search for icon. Add text. Share!'
  #Then button with text 'Icons8'

Scenario: We love SVG
Scenario: 10: Open We love SVG page and assertion
  Then click logo icon8
  Then button with text 'Спецпроекты'
  Then locate text 'Бесплатно'
  Then push link 'Open Source'
  Then scroll to end of the page
  #Then locate text 'Flat Color'
  #Then push link 'Hello World!'
  #Then locate text 'Simple jQuery Example'
  #Then locate text '!DOCTYPE html'
  #Then close popup
  Then back to previous page
  Then click logo icon8

Scenario: Web app
Scenario: 11: Open Web app page and assertion
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
  Then locate text 'емейл'
  Then locate text 'пароль'
  Then locate text 'Забыли пароль?'
  Then push link 'Регистрация'
  #Then locate text 'Register at Icons8'
  Then locate text 'емейл'
  Then locate text 'пароль'

