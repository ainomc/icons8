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

Scenario: Register
Scenario: 2: Register
  Then push link Logout
  Then push link 'Register'
  Then locate text 'Register at Icons8'
  Then add 'email' text to 'RegisterForm_email' field
  Then add 'password' text to 'RegisterForm_password' field
  Then click 'Register' element
  Then locate text 'My Account'

Scenario: Buy
Scenario: 3: Free Buy
  Then push link Logout
  Then push link in header 'Icons8'
  Then push link 'Buy'
  Then click buy 'Free' button
  Then locate text 'Register to Continue Downloading'
  Then locate 'Full name' field
  Then locate 'Email' field
  Then locate 'Password' field
  Then locate 'Create Account' element
  Then click login button in register pop-up
  Then locate text 'Login to Continue Downloading'
  Then login
  Then locate 'search icons here' field
  Then push link in header 'Icons8'

Scenario: 4: All 32,200 Icons Buy
  Then push link Logout
  Then push link in header 'Icons8'
  Then push link 'Buy'
  Then click buy 'All 33,200 Icons' button
  Then locate text 'Register to Continue Downloading'
  Then locate 'Full name' field
  Then locate 'Email' field
  Then locate 'Password' field
  Then locate 'Create Account' element
  Then click login button in register pop-up
  Then locate text 'Login to Continue Downloading'
  Then login
  Then locate text 'Paypal'
  Then locate text 'Credit cards'
  Then click 'Credit cards' button
  Then locate text 'Pay'
  Then go to Main page
  Then push link in header 'Icons8'
  Then push link 'Buy'
  Then click buy 'All 33,200 Icons' button
  Then click 'Paypal' button
  Then locate text 'CSC'
  Then go to Main page

Scenario: 5: Pay per Icon Buy
  Then push link Logout
  Then push link in header 'Icons8'
  Then push link 'Buy'
  Then click buy 'Pay per Icon' button
  Then locate text 'Register to Continue Downloading'
  Then locate 'Full name' field
  Then locate 'Email' field
  Then locate 'Password' field
  Then locate 'Create Account' element
  Then click login button in register pop-up
  Then locate text 'Login to Continue Downloading'
  Then login
  Then locate text 'Credit cards'
  Then locate text 'Paypal'
  Then go to Main page