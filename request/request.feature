Feature: Request
Scenario: Add request
Scenario: 1: Add new request
  Then go to Main page
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
  Then click logo icon8

Scenario: Check created idea
Scenario: 2: Check created idea
  Then click logo icon8
  Then push link in navigation menu 'Request'
  Then click 'Hot ideas' filter of already created ideas
  Then check ideas list in filter
  Then click 'Latest ideas' filter of already created ideas
  Then check ideas list in filter
  Then click logo icon8

Scenario: Check list of created icons ideas (short lst)
Scenario: 3: Check list of created icons ideas (short lst)
  Then click logo icon8
  Then push link in navigation menu 'Request'
  Then click 'Hot ideas' filter of already created ideas
  Then check ideas list in filter
  Then click 'Latest ideas' filter of already created ideas
  Then check ideas list in filter
  Then click 'Popular ideas' filter of already created ideas
  Then check ideas list in filter
  Then locate text 'Recently Created Icons'
  Then check recently created icons
  Then click logo icon8

Scenario: Check list of All Icon Request
Scenario: 4: Check list of All Icon Request
  Then click logo icon8
  Then push link in navigation menu 'Request'
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
  Then click logo icon8

Scenario: Fastest for $50 page
Scenario: 5: Fastest for $50 page
  Then click logo icon8
  Then push link in navigation menu 'Request'
  Then click 'Fastest for $50/icon' request icon menu
  Then locate text 'Any icon'
  Then locate text 'How Fast Is It?'
  Then locate text 'Usually, we can make 5-20 icons a day'
  Then locate text 'How Much Is It?'
  Then locate text 'To create a single icon, it will cost $50'
  Then locate text 'Where Do I Start?'
  Then push link 'Contact Us'
  Then locate text 'Contact Icons8'
  Then click logo icon8

