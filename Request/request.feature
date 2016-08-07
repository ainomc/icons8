Feature: Request
Scenario: Request Icons
Scenario: 1: Add new request
  Then push link in header 'Icons8'
  Then push link 'Request'
  Then push link 'Request Icon'
  Then locate text 'Merchant account'
  Then add text '3 Monkeys test' to 'title'
  Then push link 'Next'
  Then locate text '3 Monkeys'
  Then locate text 'How do you see this icon?'
  Then locate text 'Style'
  Then push link 'Submit'
  Then push link 'Need it Fast? Promote it'
  Then push link in header 'Icons8'


  
  







