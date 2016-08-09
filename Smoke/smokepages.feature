Feature: Open pages, login and assertions
Scenario: Open main page
Scenario: 1: Open Main page and scroll down
  Then push link in header 'Icons8'
  Then scroll to end of the page
  Then locate text 'Free Apps for the Web, Mac, and Windows'
  Then locate text 'The Community Loves Icons8'
  Then push link in header 'Icons8'

Scenario: Terms and Conditions  
Scenario: 2: Open Terms and Conditions page and assert text
  Then push link in header 'Icons8'  
  Then push link 'Terms and Conditions'
  Then scroll to end of the page
  Then locate text 'Disclaimer'
  Then locate text 'General Terms'
  Then locate text 'Our Business Model'
  Then push link in header 'Icons8'  

Scenario: Privacy Policy
Scenario: 3: Open Privacy Policy page and assertion 
  Then push link in header 'Icons8'  
  Then push link 'Privacy Policy'
  Then scroll to end of the page
  Then locate text 'Information We Collect'
  Then locate text 'Opt-Out'
  Then locate text 'Desktop version'
  Then push link in header 'Icons8'
  
Scenario: Free license
Scenario: 4: Open Free license page and assertion
  Then push link in header 'Icons8'  
  Then push link 'Free Icons'
  Then scroll to end of the page
  Then locate text 'Where to Put the Link?'
  Then locate text 'Websites'
  Then push link in header 'Icons8'

Scenario: Paid license
Scenario: 5: Open Paid license page and assertion
  Then push link in header 'Icons8'  
  Then push link 'Paid Icons'
  Then scroll to end of the page
  Then locate text 'Paid or Free, You Are Our Hero!'
  Then locate text 'Icons8 App for Mac and Windows'
  Then locate image '//cdnd.icons8.com/download/images/features_video_27.02.png'
  Then push 'Extended With API' from tabs
  Then locate text 'More Information'
  Then locate text 'Extended License in Short'
  Then push 'Students' from tabs
  Then locate text 'for free'
  Then locate text 'What Students Get'  
  Then locate image '//cdnd.icons8.com/download/images/features_video_27.02.png' 
  Then push 'Standard' from tabs  
  # Then locate image text 'Icons8 Paid Features'
  Then push link in header 'Icons8'

Scenario: Contact us
Scenario: 6: Open Contact us page and assertion
  Then push link in header 'Icons8'
  Then push link 'Contact us'
  Then scroll to end of the page
  Then locate text 'Check'
  Then locate text 'Other Questions'
  Then push link in header 'Icons8'

# # Пока ссылки на Free-icons нет, кейс заблокирован  
# # Scenario: Free icons
# # Scenario: 7: Open Free icons page and assertion 
  # # Then push link in header 'Icons8'
  # # Then scroll to end of the page
  # # Then locate text 'Free Icons'
  # # Then locate category 'airport'
  # # Then locate category 'keyboard_icons'
  # # Then push link in header 'Icons8'

Scenario: Apps Win / Mac
Scenario: 8: Open Application page and assertion
  Then push link in header 'Icons8'
  Then push link 'Download'
  Then scroll to end of the page
  Then locate text 'Download All Our Icons in a'
  Then locate text 'Download for'
  Then locate text 'Categories'
  Then push second link 'Mac'
  Then locate text 'Drag icon to Sketch'
  Then push link in header 'Icons8'

Scenario: Request icons
Scenario: 9: Open Request icons page and assertion
  Then push link in header 'Icons8'
  Then push link Request icons
  Then scroll to end of the page
  Then locate text 'Recently Created Icons'
  Then push 'Fast for $199/year' from tabs
  Then locate text 'How Fast Is It?'
  Then locate text 'Limitations'
  Then push 'Fastest for $50/icon' from tabs
  Then locate text 'Any icon, no limitations. Up to 20 icons a day. $50 per icon.'
  Then push 'Slow for Free' from tabs
# Then push 'Free for Share' in Request icons
  Then locate text 'Request Icon'
  Then push link in header 'Icons8'
  Then go to Main page

Scenario: Cosmic Pedro
Scenario: 10: Open Cosmic Pedro page and assertion
  Then push link in header 'Icons8'
  Then push link 'Resources'
  Then push link in header 'Free'
  Then locate text 'Cosmic Pedro'
  Then locate text 'Search for icon. Add text. Share!'
  #Then pedro search - пока не релазовано
  Then go to Main page

Scenario: We love SVG
Scenario: 11: Open We love SVG page and assertion
  Then push link in header 'Icons8'
  Then push link 'Resources'
  Then push link in header 'Open Source'
  Then scroll to end of the page
  Then locate text 'Flat Color'
  Then push link 'Hello World!'
  Then locate text 'Simple jQuery Example'
  Then locate element in popup
  Then close popup
  Then go to Main page

Scenario: Web app
Scenario: 12: Open Web app page and assertion
  Then push link in header 'Icons8'
  Then push link 'Icons'
  Then scroll to end of the page
  Then locate text 'New Icons'
  Then locate text 'Download'
  Then push link in header 'Icons8'
  
Scenario: Logout feature
Scenario: 13: Logout and assertion
  Then push link in header 'Icons8'
  Then push link Logout
  Then locate text 'Login'
  Then locate text 'Register' 