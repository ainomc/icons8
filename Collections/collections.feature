Feature: Collections
Scenario: Presents collections screen
Scenario: 1: Presents collections screen
  Then push link in header 'Icons8'
  Then push link 'Icons'
  Then click 'Collections' button
  Then locate text 'What can you do with collections?'
  Then locate text 'Edit and download'
  Then locate text 'Store collections'
  Then locate text 'Drag’n drop icons'
  Then locate text 'Upload SVG'
  Then push link in header 'Icons8'

Scenario: Create first collections and add collection
Scenario: 2: Create first collections and add collection
  Then push link in header 'Icons8'
  Then push link 'Icons'
  Then click 'Collections' button
  Then click 'Create collections' button
  Then add 'collection name' text to 'newCollName' field
  Then click 'confirm name' button
  Then check locate 'created first collection' element
  Then click 'first icon to collection' button
  Then check locate 'first icon in collection' element
  Then click 'first icon in collection' button
  Then click 'delete icon in collection' button
  Then push link 'Delete'
  Then locate text 'Edit and download'
  Then click 'first icon to collection' button
  Then check locate 'first icon in collection' element

Scenario: Get Font
Scenario: 3: Get Font
  Then push link in header 'Icons8'
  Then push link 'Icons'
  Then click 'Collections' button
  Then click 'Get Font' button
  Then check locate 'Get Font pop-up' element
  Then try find and check 'Unlock Font'
  Then try find and check 'Color Icons Are Excluded'
  Then push link in header 'Icons8'

Scenario: Get SVG set
Scenario: 4: Get SVG set
  Then push link in header 'Icons8'
  Then push link 'Icons'
  Then click 'Collections' button
  Then click 'Get SVG Set' button
  Then locate text 'Unlock SVG'
  Then push link 'see pricing'
  Then locate text 'Paid or Free, You Are Our Hero!'
  Then push link in header 'Icons8'

Scenario: Create Public Link
Scenario: 5: Create Public Link
  Then push link in header 'Icons8'
  Then push link 'Icons'
  Then click 'Collections' button
  Then click 'open public link pop-up' button
  Then click 'Create Public Link' element
  Then check locate 'Public Link' element
  Then push link in header 'Icons8'

Scenario: Change color (greyscale, color, custom, color palete)
Scenario: 6: Change color (greyscale, color, custom, color palete)
  Then push link in header 'Icons8'
  Then push link 'Icons'
  Then click 'Collections' button
  Then click 'open color pop-up' button
  Then locate 'grayscale' element in color pop-up
  Then locate 'color' element in color pop-up
  Then locate 'custom' element in color pop-up
  Then locate 'gray colors' element in color pop-up
  Then locate 'not gray colors' element in color pop-up
  Then click 'color palette' button
  Then locate 'color_palette' element in color pop-up
  Then locate 'canvas' element in color pop-up
  Then push link in header 'Icons8'

#Scenario: Upload icon
#Scenario: 6.1: Upload icon
  #Then push link in header 'Icons8'
  #Then push link 'Icons'
  #Then click 'Collections' button
  #Then upload 'icon' file
  #Then push link in header 'Icons8'

Scenario: Add second collections
Scenario: 7: Add second collections
  Then push link in header 'Icons8'
  Then push link 'Icons'
  Then click 'Collections' button
  Then click 'Create collections' button
  Then add 'collection name' text to 'newCollName' field
  Then click 'confirm name' button
  Then check locate 'created second collection' element
  Then click 'first icon to collection' button
  Then check locate 'first icon in collection' element
  Then click 'first icon in collection' button
  Then click 'delete icon in collection' button
  Then push link 'Delete'
  Then locate text 'Edit and download'
  Then click 'first icon to collection' button
  Then check locate 'first icon in collection' element

Scenario: Delete collections
Scenario: 8: Delete collections
  Then push link in header 'Icons8'
  Then push link 'Icons'
  Then click 'Collections' button
  Then click 'delete collection menu' button
  Then delete all 'collections' elements
  Then push link in header 'Icons8'

