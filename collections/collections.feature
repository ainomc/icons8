Feature: Collections
Scenario: Presents collections screen
Scenario: 1: Presents collections screen
  Then go to Main page
  Then push link in navigation menu 'Icons'
  Then click got it pop-up
  Then try click 'got it' button
  Then click 'Collections' button
  Then locate text 'What can you do with collections?'
  Then locate text 'Edit and download'
  Then locate text 'Store collections'
  Then locate text 'Drag’n drop icons'
  Then locate text 'Upload SVG'

Scenario: Create first collections and add collection
Scenario: 2: Create first collections and add collection
  Then go to Main page
  Then push link in navigation menu 'Icons'
  Then click got it pop-up
  Then click 'Collections' button
  Then click 'Create collections' button
  Then click 'Edit name' button
  Then add 'collection name' text to 'name field' field
  Then click 'confirm name' button
  Then check locate 'created first collection' element
  Then click 'first icon in result' button
  Then check locate 'first icon in collection' element
  Then click 'first icon in collection' button
  Then click 'delete icon in collection' button
  Then click 'delete icon' button
  Then locate text 'Edit and download'
  Then click 'first icon in result' button
  Then check locate 'first icon in collection' element

Scenario: Get Font
Scenario: 3: Get Font
  Then go to Main page
  Then push link in navigation menu 'Icons'
  Then click got it pop-up
  Then click 'Collections' button
  Then check locate 'Get Font' element

Scenario: Get SVG set
Scenario: 4: Get SVG set
  Then go to Main page
  Then push link in navigation menu 'Icons'
  Then click got it pop-up
  Then click 'Collections' button
  Then click 'Get SVG Set' button
  Then wait '.zip' file
  Then check and delete '.zip' file by extension

Scenario: Create Public Link
Scenario: 5: Create Public Link
  Then go to Main page
  Then push link in navigation menu 'Icons'
  Then click got it pop-up
  Then click 'Collections' button
  Then click 'open public link pop-up' button
  Then locate text 'Share the collection with your'

Scenario: Change color (greyscale, color, custom, color palete)
Scenario: 6: Change color (greyscale, color, custom, color palete)
  Then go to Main page
  Then push link in navigation menu 'Icons'
  Then click got it pop-up
  Then click 'Collections' button
  Then click 'open color pop-up' button
  Then locate 'grayscale' element in color pop-up
  Then locate 'color' element in color pop-up
  Then locate 'custom' element in color pop-up
  Then locate 'gray colors' element in color pop-up
  Then locate 'not gray colors' element in color pop-up
  Then click 'color palette' button

Scenario: Add second collections
Scenario: 7: Add second collections
  Then go to Main page
  Then push link in navigation menu 'Icons'
  Then click got it pop-up
  Then click 'Collections' button
  Then click 'Create collections' button
  Then click 'Edit name' button
  Then add 'collection name' text to 'name field' field
  Then click 'confirm name' button
  Then check locate 'created second collection' element
  Then click 'first icon in result' button
  Then check locate 'first icon in collection' element
  Then click 'first icon in collection' button
  Then click 'delete icon in collection' button
  Then click 'delete icon' button
  Then locate text 'Edit and download'
  Then click 'first icon in result' button
  Then check locate 'first icon in collection' element

Scenario: Delete collections
Scenario: 8: Delete collections
  Then go to Main page
  Then push link in navigation menu 'Icons'
  Then click got it pop-up
  Then click 'Collections' button
  Then click 'delete collection menu' button
  Then delete all 'collections' elements
