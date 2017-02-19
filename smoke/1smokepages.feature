Feature: Open pages, login and assertions
Scenario: Open main page
Scenario: 1: Open Main page and scroll down
  Then click logo icon8
  Then scroll to end of the page
  Then locate text 'Free Apps for the Web, Mac, and Windows'
  Then locate text 'The Community Loves Icons8'
  Then click logo icon8

Scenario: Terms and Conditions
Scenario: 2: Open Terms and Conditions page and assert text
  Then click logo icon8
  Then push link 'Terms and Conditions'
  Then scroll to end of the page
  Then locate text 'Disclaimer'
  Then locate text 'General Terms'
  Then locate text 'Our Business Model'
  Then locate text 'Free License'
  Then locate text 'Buy Full License'
  Then locate text 'Desktop version'
  Then click logo icon8

Scenario: Privacy Policy
Scenario: 3: Open Privacy Policy page and assertion
  Then click logo icon8
  Then push link 'Privacy Policy'
  Then scroll to end of the page
  Then locate text 'Information We Collect'
  Then locate text 'Opt-Out'
  Then locate text 'Our Business Model'
  Then locate text 'Free License'
  Then locate text 'Buy Full License'
  Then locate text 'Desktop version'
  Then click logo icon8

Scenario: Free license
Scenario: 4: Open Free license page and assertion
  Then click logo icon8
  Then button with text 'Free License'
  Then scroll to end of the page
  Then locate text 'Use Icons for Free'
  Then locate text 'Why to Link?'
  Then locate text 'Where to Put the Link?'
  Then locate text 'Websites'
  Then locate text 'Desktop Apps'
  Then locate text 'Mobile Apps'
  Then locate text 'Open Source'
  Then click logo icon8


Scenario: Paid license
Scenario: 5: Open Paid license page and assertion
  Then click logo icon8
  Then push link 'Buy Full License'
  Then scroll to end of the page
  Then locate text 'Paid or Free, You Are Our Hero'
  Then locate text 'Paid License Summary'
  Then locate text 'Prohibited Uses for all Licenses'
  Then locate text 'What's Included'
  Then locate text 'Built-in Editing Tools'
  Then locate text 'Icons8 App for Mac and Windows'
  Then locate image '//cdnd.icons8.com/download/images/features_video_27.02.png'
  Then click logo icon8

Scenario: Contact us
Scenario: 6: Open Contact us page and assertion
  Then click logo icon8
  Then push link 'Contact us'
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
  Then locate text 'Download Icons8 for'
  Then locate text 'Other Versions'
  Then locate text 'Features'
  Then locate text 'How it Works'
  Then locate text 'All the Icons You Need'
  Then locate text 'Most Popular'
  Then locate text 'View all'
  Then locate text 'Features for UI Designers'
  Then locate text 'Single Style'
  Then locate text 'Editable Vectors'
  Then locate text 'Icon Recoloring'
  Then locate text 'Daily Updates Guided'
  Then locate text 'The Community'
  Then click logo icon8

Scenario: Request icons
Scenario: 8: Open Request icons page and assertion
  Then click logo icon8
  Then push link in navigation menu 'Request'
  Then locate concrete text 'Request Icons'
  Then locate text 'Hot Ideas'
  Then locate text 'Latest Ideas'
  Then locate text 'Popular Ideas'
  Then locate text 'View all icon ideas'
  Then locate text 'Recently'
  Then push 'Fast for $199/year' from tabs
  Then locate text 'How Fast'
  Then locate text 'Limitations'
  Then locate text 'Good For Fast Track'
  Then locate text 'Bad For Fast Track'
  Then push 'Fastest for $50/icon' from tabs
  Then locate text 'How Fast Is It?'
  Then locate text 'How Much Is It?'
  Then locate text 'Where Do I Start?'
  Then locate text 'Any icon, no limitations. Up to 20 icons a day. $50 per icon.'
  Then push 'Slow for Free' from tabs
  Then locate text 'Recently '
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
  Then go to Main page
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
  Then push link in navigation menu 'Icons'
  Then scroll to end of the page
  Then locate text 'New Icons'
  Then locate text 'Download'
  Then locate text 'Generate HTML'
  Then locate text 'Icon'
  Then click logo icon8

Scenario: Account/Profile
Scenario: 12: Account/Profile
  Then click logo icon8
  Then push link 'My Account'
  Then locate concrete text 'Account'
  Then locate concrete text 'Your current plan'
  Then push link 'Downloads'
  Then locate text 'ZIP Files'
  Then locate text 'Icons8 App'
  Then click 'API' button
  Then locate text 'API endpoint'
  Then locate text 'API Auth Token'
  Then click 'Profile' button
  Then locate text 'change email or password'

Scenario: Logout feature
Scenario: 13: Logout and assertion
  Then click logo icon8
  Then push link Logout
  Then locate text 'Login'
  Then locate text 'Register'

