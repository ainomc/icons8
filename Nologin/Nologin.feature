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
  Then locate 'Full name' field
  Then locate 'Full name' field
  Then locate 'Create Account' element
  Then click login button in register pop-up
  Then locate text 'Login to Continue Downloading'
  Then login
  #Then locate text 'Need it Fast? Promote it'
  #Then locate text 'Skip'
  # На демо версии сайта после логине, при создании идеи, вечная загрузка
  Then push link in header 'Icons8'
