Feature: User without login
Scenario: Request new icon without login
Scenario: 1: Request new icon without login
  Then click logo icon8
  Then push link Logout
  Then push link in navigation menu 'Request'
  Then push button what named 'Request Icon'
  Then locate text 'Merchant account'
  Then add text to 'title'
  Then clear similar ideas
  Then push button 'Next'
  Then locate text 'How do you see this icon?'
  Then locate text 'Style'
  Then choose style of request icon
  Then push button what named 'Submit'
  Then locate text 'Register to Continue Downloading'
  Then find 'RegisterForm_name' element
  Then find 'RegisterForm_email' element
  Then find 'RegisterForm_password' element
  Then locate 'Create Account' element
  Then click login button in register pop-up
  Then locate text 'Login to Continue Downloading'
  Then login
  Then locate text 'Need it Fast? Promote it'
  Then locate text 'Skip'
  Then click logo icon8

Scenario: Register
Scenario: 2: login during Register
  Then go to Main page
  Then push link Logout
  Then push link 'Register'
  Then locate text 'Register at Icons8'
  Then add 'email' text to 'RegisterForm_email' field
  Then add 'password' text to 'RegisterForm_password' field
  Then click 'Register' element
  Then locate text 'My Account'
  Then go to Main page

Scenario: Buy
Scenario: 3: login during  free Buy
  Then go to Main page
  Then push link Logout
  Then go to Main page
  Then push link 'Buy'
  Then click buy 'Free' button
  Then locate text 'Register to Continue Downloading'
  Then find 'RegisterForm_name' element
  Then find 'RegisterForm_email' element
  Then find 'RegisterForm_password' element
  Then locate 'Create Account' element
  Then click login button in register pop-up
  Then locate text 'Login to Continue Downloading'
  Then login
  Then locate 'Search icons' field
  Then click logo icon8

Scenario: 4: login during  All 32,200 Icons Buy
  Then go to Main page
  Then push link Logout
  Then go to Main page
  Then push link 'Buy'
  Then click buy 'All 33,100 Icons' button
  Then locate text 'Register to Continue Downloading'
  Then find 'RegisterForm_name' element
  Then find 'RegisterForm_email' element
  Then find 'RegisterForm_password' element
  Then locate 'Create Account' element
  Then click login button in register pop-up
  Then locate text 'Login to Continue Downloading'
  Then login
  Then locate text 'Paypal'
  Then locate text 'Credit cards'
  Then click 'Credit cards' button
  Then locate text 'Pay'
  Then go to Main page
  Then click logo icon8
  Then push link 'Buy'
  Then click buy 'All 33,100 Icons' button
  Then click 'Paypal' button
  Then locate text '1999-2017'
  Then go to Main page

Scenario: 5: login during Pay per Icon Buy
  Then go to Main page
  Then push link Logout
  Then go to Main page
  Then push link 'Buy'
  Then click buy 'Pay per Icon' button
  Then locate text 'Register to Continue Downloading'
  Then find 'RegisterForm_name' element
  Then find 'RegisterForm_email' element
  Then find 'RegisterForm_password' element
  Then locate 'Create Account' element
  Then click login button in register pop-up
  Then locate text 'Login to Continue Downloading'
  Then login
  Then locate text 'Credit cards'
  Then locate text 'Paypal'
  Then go to Main page

#Scenario: 6: Login during downloading
  #Then push link Logout
  #Then click logo icon8
  #Then push link 'Download'
  #Then click 'Download for Windows' button
  #Then locate text 'Register to Continue Downloading'
  #Then find 'RegisterForm_name' element
  #Then find 'RegisterForm_email' element
  #Then find 'RegisterForm_password' element
  #Then locate 'Create Account' element
  #Then click login button in register pop-up
  #Then locate text 'Login to Continue Downloading'
  #Then login
  #Then locate text 'How likely you would'
  #Then click 'recommend' button
  #Then locate text 'Download is Starting Now'
  #Then locate text 'click here'
  #Then click logo icon8