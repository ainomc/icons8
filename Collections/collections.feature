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

Scenario: Delete collections
Scenario: 12: Delete collections
  Then push link in header 'Icons8'
  Then push link 'Icons'
  Then click 'Collections' button
  Then click 'delete collection menu' button
  Then delete all 'collections' elements
  Then push link in header 'Icons8'

"""
Scenario: 0: Collections are in the right bar
  Then push link 'Icons'
#  Then push button 'Got It'
  Then push unactive tab
  
Scenario: 1: Create collection
  Then push 'Create'
  Then enter name "Auto Collection 100"
  Then push button "Done"
  Then push button 'Create'
  Then push button "Done"
"""
  
# Scenario: 28: Delete collection
  # Then push button 'Edit collection'
  # Then push button 'Delete collection'
  # Then push button 'Cancel'
  # Then push button 'Delete collection'
  # Then push button 'Delete'
  # Then push button 'Delete collection'
  # Then push button 'Delete'
  # Then push button "Finish edit"
  
  
  
  
# Add icons to a collection (native icons)
# Icon name of an icon in the collection                                                                                                                                                                                                                                                        
# Drag'n'drop icons to collections
# Upload my SVG into collections                                                                                                                                                                                                                                                        
# Rename collection
# Download icons in all formats including fonts
# When downloading the collection, all icons should be downloaded, not only selected ones
# Resizing and recoloring the icons, downloading
# Removing icons from a collection (both uloaded and native)
# Sharing a collection (link, FB, twitter)
# Checking a shared collection (link, FB, twitter)
# Шаринг приватных коллекций
# Other user adds a collection to his account
# Manage collections from two different browsers
# Синхронизация коллекций
# Notification dialog text and design after sync
# Remove icons from a collection
# Front end of the collection (web view)
# " When icons are deleted from the collection, the selection in the center panel must be deleted too

# https://visualpharm.atlassian.net/browse/ICONS-405"
# Ограничения: 50 коллекций, 1000 иконок в коллекции
# у незаголиненного юзера - ограничение меньше, д.б. сообщение о достижении лимита
# есть сообщение о недоступности новых иконок, если истекла лиценцзия у юзера (старые должны быть доступны)
# Кнопки GetFont и GetSVG доступны только юзерам с доступами
# Можно импортировать иконки, они будут доступны в твоём профиле всегда
# Удаление коллекциий