Feature: Search
Scenario: Search test on main page
Scenario: 1: Positive search test on main page
  Then click logo icon8
  Then click 'search' field
  Then add 'positive text' text to 'search' field
  Then click 'search' button
  Then check locate 'icons result' element
  Then click 'search platform filter' button
  Then locate text 'Generate HTML'
  Then click logo icon8

Scenario: Search test on main page
Scenario: 2: Negative search test on main page
  Then click logo icon8
  Then click 'search' field
  Then add 'negative text' text to 'search' field
  Then click 'search' button
  Then absent 'search result' element
  Then locate text 'Nothing found'
  Then locate text 'Request icons'
  Then click logo icon8

Scenario: Search on platform icons pack page
Scenario: 3: Positive search test on iOS9 Icon Pack page
  Then click logo icon8
  Then choose 'iOS9 Icon Pack' element
  Then locate text 'All the iOS 10 Icons You Need.'
  Then click 'search' field
  Then add 'positive text' text to 'search' field
  Then click 'search' button
  Then check locate 'icons result' element
  Then locate text 'Generate HTML'
  Then click logo icon8

Scenario: Search on platform icons pack page
Scenario: 4: Negative search test on iOS9 Icon Pack page
  Then click logo icon8
  Then choose 'iOS9 Icon Pack' element
  Then click 'search' field
  Then add 'negative text' text to 'search' field
  Then click 'search' button
  Then absent 'search result' element
  Then locate text 'Nothing found'
  Then locate text 'Request icons'
  Then click logo icon8

Scenario: Search on platform icons pack page
Scenario: 5: Positive search test on Android 4 Icon Pack
  Then click logo icon8
  Then choose 'Android 4 Icon Pack' element
  Then locate text 'All the Android 4 Icons You Need.'
  Then click 'search' field
  Then add 'positive text' text to 'search' field
  Then click 'search' button
  Then check locate 'icons result' element
  Then locate text 'Generate HTML'
  Then click logo icon8

Scenario: Search on platform icons pack page
Scenario: 6: Negative search test on Android 4 Icon Pack
  Then click logo icon8
  Then choose 'Android 4 Icon Pack' element
  Then click 'search' field
  Then add 'negative text' text to 'search' field
  Then click 'search' button
  Then absent 'search result' element
  Then locate text 'Nothing found'
  Then locate text 'Request icons'
  Then click logo icon8

Scenario: Search on platform icons pack page
Scenario: 7: Positive search test on Material Icon Pack
  Then click logo icon8
  Then choose 'Material Icon Pack' element
  Then locate text 'All the Material Icons You Need.'
  Then click 'search' field
  Then add 'positive text' text to 'search' field
  Then click 'search' button
  Then check locate 'icons result' element
  Then locate text 'Generate HTML'
  Then click logo icon8

Scenario: Search on platform icons pack page
Scenario: 8: Negative search test on Material Icon Pack
  Then click logo icon8
  Then choose 'Material Icon Pack' element
  Then click 'search' field
  Then add 'negative text' text to 'search' field
  Then click 'search' button
  Then absent 'search result' element
  Then locate text 'Nothing found'
  Then locate text 'Request icons'
  Then click logo icon8

Scenario: Search on platform icons pack page
Scenario: 9: Positive search test on Windows 8 Icon Pack
  Then click logo icon8
  Then choose 'Windows 8 Icon Pack' element
  Then locate text 'All the Windows 8 Icons You Need.'
  Then click 'search' field
  Then add 'positive text' text to 'search' field
  Then click 'search' button
  Then check locate 'icons result' element
  Then locate text 'Generate HTML'
  Then click logo icon8

Scenario: Search on platform icons pack page
Scenario: 10: Negative search test on Windows 8 Icon Pack
  Then click logo icon8
  Then choose 'Windows 8 Icon Pack' element
  Then click 'search' field
  Then add 'negative text' text to 'search' field
  Then click 'search' button
  Then absent 'search result' element
  Then locate text 'Nothing found'
  Then locate text 'Request icons'
  Then click logo icon8

Scenario: Search on platform icons pack page
Scenario: 11: Positive search test on Windows 10 Icon Pack
  Then click logo icon8
  Then choose 'Windows 10 Icon Pack' element
  Then locate text 'All the Windows 10 Icons You Need.'
  Then click 'search' field
  Then add 'positive text' text to 'search' field
  Then click 'search' button
  Then check locate 'icons result' element
  Then locate text 'Generate HTML'
  Then click logo icon8

Scenario: Search on platform icons pack page
Scenario: 12: Negative search test on Windows 10 Icon Pack
  Then click logo icon8
  Then choose 'Windows 10 Icon Pack' element
  Then click 'search' field
  Then add 'negative text' text to 'search' field
  Then click 'search' button
  Then absent 'search result' element
  Then locate text 'Nothing found'
  Then locate text 'Request icons'
  Then click logo icon8

Scenario: Search on platform icons pack page
Scenario: 13: Positive search test on Flat Color Icon Pack
  Then click logo icon8
  Then choose 'Flat Color Icon Pack' element
  Then locate text 'All the Flat Color Icons You Need.'
  Then click 'search' field
  Then add 'positive text' text to 'search' field
  Then click 'search' button
  Then check locate 'icons result' element
  Then locate text 'Generate HTML'
  Then click logo icon8

Scenario: Search on platform icons pack page
Scenario: 14: Negative search test on Flat Color Icon Pack
  Then click logo icon8
  Then choose 'Flat Color Icon Pack' element
  Then click 'search' field
  Then add 'negative text' text to 'search' field
  Then click 'search' button
  Then absent 'search result' element
  Then locate text 'Nothing found'
  Then locate text 'Request icons'
  Then click logo icon8

Scenario: Search on platform icons pack page
Scenario: 15: Positive search test on Office Icon Pack
  Then click logo icon8
  Then choose 'Office Icon Pack' element
  Then locate text 'All the Office Icons You Need.'
  Then click 'search' field
  Then add 'positive text' text to 'search' field
  Then click 'search' button
  Then check locate 'icons result' element
  Then locate text 'Generate HTML'
  Then click logo icon8

Scenario: Search on platform icons pack page
Scenario: 16: Negative search test on Office Icon Pack
  Then click logo icon8
  Then choose 'Office Icon Pack' element
  Then click 'search' field
  Then add 'negative text' text to 'search' field
  Then click 'search' button
  Then absent 'search result' element
  Then locate text 'Nothing found'
  Then locate text 'Request icons'
  Then click logo icon8

Scenario: Search filters
Scenario: 17: Search filters
  Then click logo icon8
  Then click 'search' field
  Then add 'positive text' text to 'search' field
  Then click 'search' button
  Then check locate 'icons result' element
  Then click on filter '1'
  Then check locate 'simple list' element
  Then click on filter '2'
  Then check locate 'list with names' element
  Then try click 'got it' button
  Then click on filter '3'
  Then check locate 'table list' element
  Then click logo icon8
