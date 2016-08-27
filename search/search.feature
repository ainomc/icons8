Feature: Search
Scenario: Search test on main page
Scenario: 1: Positive search test on main page
  Then push link in header 'Icons8'
  Then click 'search' field
  Then add 'positive text' text to 'search' field
  Then click on 'search' button
  Then check locate 'search result' element
  Then push link in header 'Icons8'

Scenario: Search test on main page
Scenario: 2: Negative search test on main page
  Then push link in header 'Icons8'
  Then click 'search' field
  Then add 'negative text' text to 'search' field
  Then click on 'search' button
  Then absent 'search result' element
  Then push link in header 'Icons8'

