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

Scenario: Check list of created icons ideas (short lst)
Scenario: 2: Check list of created icons ideas (short lst)
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

Scenario: Check list of All Icon Request
Scenario: 3: Check list of All Icon Request
  Then push link in header 'Icons8'
  Then push link 'Request'
  Then push link 'View all icon ideas'
  Then locate text 'All Icon Request'
  Then locate text 'Style'
  Then locate text 'ossible Matches'
  Then click 'Hot ideas' filter of already created ideas
  Then check ideas list
  Then click 'Latest ideas' filter of already created ideas
  Then check ideas list
  Then click 'Popular ideas' filter of already created ideas
  Then check ideas list
  Then push link in header 'Icons8'

  Scenario: Buy fast track page
  Scenario: 4: Buy fast track page
  Then push link in header 'Icons8'
  Then push link 'Request'
  Then click 'Fast for $199/year' request icon menu
  Then locate text 'How Fast Is It'
  Then locate image '/static/images/request/fast-track.jpg'
  Then locate text 'Limitations'
  Then locate text 'You can only order one icon every two days'
  Then locate text 'Icons should be generic'
  Then locate text 'Good For Fast Track'
  Then locate text 'Bad For Fast Track'
  Then locate image '/static/images/request/fast-track-good.jpg'
  Then locate image '/static/images/request/fast-track-bad.jpg'
  Then locate text '2Checkout.com Inc'
  Then locate text 'If you need a specific icon'
  Then push link 'Buy Fast Track'
  Then locate text 'Fast Track'
  Then locate text 'Unit Price'
  Then go to Main page

