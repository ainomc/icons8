Feature: Open pages, login and assertions
Scenario: Choose german localisation
Scenario: 1: Choose german localisation
  Then go to Main page
  Then click 'selectLanguage' button element
  Then push link 'German'

Scenario: Terms and Conditions
Scenario: 2: Open Terms and Conditions page and assert text
  Then click logo icon8
  Then push link 'Geschäftsbedinungen'
  Then scroll to end of the page
  Then locate text 'Unser Geschäftsmodell'
  Then locate text 'Kostenlose Lizenz'
  Then locate text 'Volle Lizenz kaufen'
  Then locate text 'Desktop Version'
  Then click logo icon8

Scenario: Privacy Policy
Scenario: 3: Open Privacy Policy page and assertion
  Then click logo icon8
  Then push link 'Datenschutzrichtlinien'
  Then scroll to end of the page
  Then locate text 'Unser Geschäftsmodell'
  Then locate text 'Kostenlose Lizenz'
  Then locate text 'Volle Lizenz kaufen'
  Then locate text 'Desktop Version'
  Then click logo icon8

Scenario: Free license
Scenario: 4: Open Free license page and assertion
  Then click logo icon8
  Then click 'Kostenlose Icons' button
  Then locate text 'Verwende die Icons'
  Then locate text 'Warum verlinken?'
  Then locate text 'Wohin soll der Link?'
  Then locate text 'Webseiten'
  Then locate text 'Desktop Applikationen'
  Then locate text 'Apps für Mobile Geräte'
  Then locate text 'Open Source'
  Then click logo icon8

Scenario: Paid license
Scenario: 5: Open Paid license page and assertion
  Then click logo icon8
  Then push link 'Bezahlte Symbole'
  Then scroll to end of the page
  Then locate text 'Bezahlt oder gratis, du bist unser Held'
  Then locate text 'Zusammenfassung der kostenpflichtigen Lizenz'
  Then locate text 'Untersagte Verwendungszwecke für alle Lizenzen'
  Then locate text 'Was ist enthalten'
  Then locate text 'Integrierte Bearbeitungswerkzeuge'
  Then locate text 'Icons8 App für Mac und Windows'
  Then locate image '//cdnd.icons8.com/download/images/features_video_27.02.png'
  Then click logo icon8

Scenario: Contact us
Scenario: 6: Open Contact us page and assertion
  Then click logo icon8
  Then push link 'Kontaktiere uns'
  Then scroll to end of the page
  Then locate text 'Contact Icons8'
  Then locate text 'Talk to a Human'
  Then locate text 'Our support team consists'
  Then click logo icon8

Scenario: Apps Win / Mac
Scenario: 7: Open Application page and assertion
  Then click logo icon8
  Then click 'Download menu' button
  Then click 'icon8 app in download pop-up' button
  Then scroll to end of the page
  Then locate text 'Lade alle Icons mit unserer '
  Then locate text 'Download für'
  Then locate text 'Alle Icons, die du brauchst'
  Then locate text 'Am beliebtesten'
  Then locate text 'Alle anzeigen'
  Then locate text 'Konsistente Stilrichtung'
  Then locate text 'Editierbare Vektorengrafiken '
  Then locate text 'Icons umfärben'
  Then locate text 'Tägliche Updates'
  Then locate text 'Die Community'
  Then click logo icon8

Scenario: Request icons
Scenario: 8: Open Request icons page and assertion
  Then click logo icon8
  Then push link 'Anfragen'
  Then scroll to end of the page
  Then locate text 'Icons anfordern'
  Then locate text 'Beliebte Ideen'
  Then locate text 'Neueste Ideen'
  Then locate text 'Populäre Ideen'
  Then locate text 'Alle Icon Ideen'
  Then locate text 'Zuletzt erstellte'
  Then push 'Schnell für $50/Icon' from tabs
  Then locate text 'Wie schnell ist es?'
  Then locate text 'Wie viel kostet das?'
  Then locate text 'Wo soll ich anfangen?'
  Then locate text 'Jedes Icon, keine Einschränkungen. Bis zu 20 Symbole pro Tag. $50 pro Icon'
  Then push 'Langsam, aber kostenlos' from tabs
  Then locate text 'Zuletzt erstellte'
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
  Then push link 'German'

  Then click logo icon8
  Then push link in navigation menu 'Symbole'
  Then scroll to end of the page
  Then locate text 'New Icons'
  Then locate text 'Download'
  Then locate text 'HTML erstellen'
  Then locate text 'Icon'
  Then click logo icon8

Scenario: Logout feature
Scenario: 12: Logout and assertion
  Then click logo icon8
  Then locate text 'Mein Konto'
  Then push link Logout
  Then click logo icon8
  Then push link 'Anmelden'
  Then locate text 'Bei Icons8 anmelden'
  Then locate text 'Passwort vergessen?'
  Then push link 'Registrieren'