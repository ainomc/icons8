Feature: Request
Scenario: Add request
Scenario: 1: Add new request
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
  Then locate text 'Need it Fast? Promote it'
  Then locate text 'Skip'
  Then push link in header 'Icons8'

Scenario: Check created icons ideas
Scenario: 2: Check created icons ideas
  Then push link in header 'Icons8'
  Then push link 'Request'
  Then click 'Hot ideas' filter of already created ideas
  Then check ideas list in filter
  Then click 'Latest ideas' filter of already created ideas
  Then check ideas list in filter
  Then click 'Popular ideas' filter of already created ideas
  Then check ideas list in filter
  Then locate text 'Recently Created Icons'
  Then check recently created icons
  Then push link in header 'Icons8'

  
  







