Feature: Collections
Scenario: Create collection
Scenario: 0: Collections are in the right bar
  Then push link 'Icons'
  Then push "Got it" into Notification bar
  Then push tab 'Collections'
  
Scenario: 1: Create collection
  Then push button 'Create'
  Then enter name "Auto Collection 100"
  Then push button "Done"
  Then push button 'Create'
  Then push button "Done"
  
Scenario: 28: Delete collection
  Then push button 'Edit collection'
  Then push button 'Delete collection'
  Then push button 'Cancel'
  Then push button 'Delete collection'
  Then push button 'Delete'
  Then push button 'Delete collection'
  Then push button 'Delete'
  Then push button "Finish edit"
  
  
  
  
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