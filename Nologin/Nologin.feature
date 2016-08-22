Feature: User without login
Scenario: Request new icon without login
Scenario: 1: Request new icon without login
  Then push link Logout
  Then push link in header 'Icons8'
  Then push link 'Request'
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
  Then locate 'Full name' field
  Then locate 'Email' field
  Then locate 'Password' field
  Then locate 'Create Account' element
  Then click login button in register pop-up
  Then locate text 'Login to Continue Downloading'
  Then login
  Then locate text 'Need it Fast? Promote it'
  Then locate text 'Skip'
  Then push link in header 'Icons8'

#Scenario: Buy
#Scenario: 2: Free Buy
  #Then push link Logout
  #Then push link in header 'Icons8'
  #Then push link 'Buy'
  #Then click 'Get' on 'Free' block
  #Then locate text 'Register to Continue Downloading'
  #Then locate 'Full name' field
  #Then locate 'Email' field
  #Then locate 'Password' field
  #Then locate 'Create Account' element
  #Then click login button in register pop-up
  #Then locate text 'Login to Continue Downloading'
  #Then login
  #Then locate 'search icons here' field
  #Then push link in header 'Icons8'


#Scenario: 3: All 32,200 Icons Buy
  #Then push link Logout
  #Then push link in header 'Icons8'
  #Then push link 'Buy'
  #Then click 'Buy' on 'All 32,200 Icons' block
  #Then locate text 'Register to Continue Downloading'
  #Then locate 'Full name' field
  #Then locate 'Email' field
  #Then locate 'Password' field
  #Then locate 'Create Account' element
  #Then click login button in register pop-up
  #Then locate text 'Login to Continue Downloading'
  #Then login
  #Then locate text 'Credit cards'
  #Then locate text 'Paypal'
  #Then push link in header 'Icons8'

#Scenario: 4: Pay per Icon Buy
  #Then push link Logout
  #Then push link in header 'Icons8'
  #Then push link 'Buy'
  #Then click 'Buy' on 'Pay per Icon Buy' block
  #Then locate text 'Register to Continue Downloading'
  #Then locate 'Full name' field
  #Then locate 'Email' field
  #Then locate 'Password' field
  #Then locate 'Create Account' element
  #Then click login button in register pop-up
  #Then locate text 'Login to Continue Downloading'
  #Then login
  #Then locate text 'Credit cards'
  #Then locate text 'Paypal'
  #Then push link in header 'Icons8'