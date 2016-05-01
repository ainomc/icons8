Feature: Open pages and assertions
# Scenario: Open main page
# Scenario: 1: Open Main page and scroll down
  # Then push link in header 'Icons8'
  # Then scroll to end of the page
  # Then locate text 'Free Apps for the Web, Mac, and Windows'
  # Then locate text 'The Community Loves Icons8'
  # Then push link in header 'Icons8'

# Scenario: Terms and Conditions  
# Scenario: 2: Open Terms and Conditions page and assert text
  # Then push link in header 'Icons8'  
  # Then push link 'Terms and Conditions'
  # Then scroll to end of the page
  # Then locate text 'Disclaimer'
  # Then locate text 'General Terms'
  # Then locate text 'Our Business Model'
  # Then push link in header 'Icons8'  

# Scenario: Privacy Policy
# Scenario: 3: Open Privacy Policy page and assertion 
  # Then push link in header 'Icons8'  
  # Then push link 'Privacy Policy'
  # Then scroll to end of the page
  # Then locate text 'Information We Collect'
  # Then locate text 'Opt-Out'
  # Then locate text 'Desktop version'
  # Then push link in header 'Icons8'
  
# Scenario: Free license
# Scenario: 4: Open Free license page and assertion
  # Then push link in header 'Icons8'  
  # Then push link 'Free Icons'
  # Then scroll to end of the page
  # Then locate text 'Where to Put the Link?'
  # Then locate text 'Websites'
  # Then push link in header 'Icons8'

# Scenario: Paid license
# Scenario: 5: Open Paid license page and assertion
  # Then push link in header 'Icons8'  
  # Then push link 'Paid Icons'
  # Then scroll to end of the page
  # Then locate text 'Paid or Free, You Are Our Hero!'
  # Then locate text 'Icons8 App for Mac and Windows'
  # Then locate image '//cdnd.icons8.com/download/images/features_video_27.02.png'
 # # Then locate image text 'Icons8 Paid Features'
  # Then push link in header 'Icons8'

# Scenario: Contact us
# Scenario: 6: Open Contact us page and assertion
  # Then push link in header 'Icons8'
  # Then push link 'Contact us'
  # Then scroll to end of the page
  # Then locate text 'Check'
  # Then locate text ' a message'
  # Then push link in header 'Icons8'

# # Пока ссылки на Free-icons нет, кейс заблокирован  
# Scenario: Free icons
# Scenario: 7: Open Free icons page and assertion 
  # Then push link in header 'Icons8'
  # Then scroll to end of the page
  # Then locate text 'Free Icons'
  # Then locate category 'airport'
  # Then locate category 'keyboard_icons'
  # Then push link in header 'Icons8'

# Scenario: Apps Win / Mac
# Scenario: 8: Open Application page and assertion
  # Then push link in header 'Icons8'
  # Then push link 'Download'
  # Then scroll to end of the page
  # Then locate text 'Pick your color, size, and format. Drag it to Photoshop. Done.'
  # Then locate text 'How it Works'
  # Then locate text 'Download Icons8 App for Windows'
  # Then push link 'Mac OS'
  # Then locate text 'Download Icons8 App for Mac'
  # Then push link in header 'Icons8'

Scenario: Request icons
Scenario: 9: Open Request icons page and assertion
  Then push link in header 'Icons8'
  Then push link request 'Browse for ideas or request an icon'  
  Then scroll to end of the page
  Then locate text 'Recently Created Icons'
  Then push link 'Fast track'
  Then locate text 'How Does It Work?'
  Then locate text 'Buy Fast Track'
  Then push link 'Custom'  
  Then push link in header 'Icons8'

# Scenario: Web app
# Scenario: 10: Open Web app page ...
  # Then push link in header 'Icons8'
  # Then scroll to end of the page
  # Then locate text 'Free Apps for the Web, Mac, and Windows'
  # Then locate text 'The Community Loves Icons8'
# Scenario: Open main page
  
# Scenario: 99: Create collection
  # Then push 'Create'
  # Then enter name 'Auto Collection 100'
  # Then push button 'Done'
  # Then push button 'Create'
  # Then push button 'Done'