Feature: Download tests
Scenario: Download windows app
Scenario: 1: Download windows app
  Then go to Main page
  Then click 'Download menu' button
  Then click 'icon8 app in download pop-up' button
  Then push link 'Download Icons8 for Windows'
  Then sleep '4' seconds
  Then wait downloading end of 'part' file
  Then check and delete '.exe' file by extension
  Then go to Main page

Scenario: Simple download icon
Scenario: 2: Simple download icon
  Then go to Main page
  Then push link in navigation menu 'Icons'
  Then click 'Download in icon bar' button
  Then try push text 'Free Download'
  Then sleep '30' seconds
  Then check and delete '.png' file by extension
  Then go to Main page

Scenario: Download PNG 50 px
Scenario: 3: Download PNG 50 px
  Then go to Main page
  Then push link in navigation menu 'Icons'
  Then click 'Open download icon pop-up' button
  Then move mouse to 'right bar' element
  Then choose '1' button in download pop-up
  Then choose 'PNG' download icon type in download pop-up
  Then click 'Download in icon bar' button
  Then try push text 'Free Download'
  Then sleep '30' seconds
  Then check and delete '.png' file by extension
  Then go to Main page

Scenario: Download PNG 100 px
Scenario: 4: Download PNG 100 px
  Then go to Main page
  Then push link in navigation menu 'Icons'
  Then click 'Open download icon pop-up' button
  Then choose '2' button in download pop-up
  Then choose 'PNG' download icon type in download pop-up
  Then click 'Download in icon bar' button
  Then try push text 'Free Download'
  Then sleep '30' seconds
  Then check and delete '.png' file by extension
  Then go to Main page

Scenario: Download PNG 500 px
Scenario: 5: Download PNG 500 px
  Then go to Main page
  Then push link in navigation menu 'Icons'
  Then click 'Open download icon pop-up' button
  Then choose '3' button in download pop-up
  Then choose 'PNG' download icon type in download pop-up
  Then click 'Download in icon bar' button
  Then try push text 'Free Download'
  Then sleep '10' seconds
  Then check and delete '.png' file by extension
  Then go to Main page

Scenario: Download SVG 50 px
Scenario: 6: Download SVG 50 px
  Then go to Main page
  Then push link in navigation menu 'Icons'
  Then click 'Open download icon pop-up' button
  Then move mouse to 'right bar' element
  Then choose '1' button in download pop-up
  Then choose 'SVG' download icon type in download pop-up
  Then click 'Download in icon bar' button
  Then try push text 'Free Download'
  Then sleep '10' seconds
  Then check and delete '.svg' file by extension
  Then go to Main page

Scenario: Download SVG 100 px
Scenario: 7: Download SVG 100 px
  Then go to Main page
  Then push link in navigation menu 'Icons'
  Then click 'Open download icon pop-up' button
  Then choose '2' button in download pop-up
  Then choose 'SVG' download icon type in download pop-up
  Then click 'Download in icon bar' button
  Then try push text 'Free Download'
  Then sleep '10' seconds
  Then check and delete '.svg' file by extension
  Then click logo icon8

Scenario: Download SVG 500 px
Scenario: 8: Download SVG 500 px
  Then go to Main page
  Then push link in navigation menu 'Icons'
  Then click 'Open download icon pop-up' button
  Then choose '3' button in download pop-up
  Then choose 'SVG' download icon type in download pop-up
  Then click 'Download in icon bar' button
  Then try push text 'Free Download'
  Then sleep '10' seconds
  Then check and delete '.svg' file by extension
  Then go to Main page

Scenario: Download EPS 50 px
Scenario: 9: Download EPS 50 px
  Then go to Main page
  Then push link in navigation menu 'Icons'
  Then click 'Open download icon pop-up' button
  Then move mouse to 'right bar' element
  Then choose '1' button in download pop-up
  Then choose 'EPS' download icon type in download pop-up
  Then click 'Download in icon bar esp' button
  Then try push text 'Free Download'
  Then sleep '10' seconds
  Then check and delete '.eps' file by extension
  Then go to Main page

Scenario: Download EPS 100 px
Scenario: 10: Download EPS 100 px
  Then go to Main page
  Then push link in navigation menu 'Icons'
  Then click 'Open download icon pop-up' button
  Then choose '2' button in download pop-up
  Then choose 'EPS' download icon type in download pop-up
  Then click 'Download in icon bar esp' button
  Then try push text 'Free Download'
  Then sleep '10' seconds
  Then check and delete '.eps' file by extension
  Then go to Main page

Scenario: Download EPS 500 px
Scenario: 11: Download EPS 500 px
  Then go to Main page
  Then push link in navigation menu 'Icons'
  Then click 'Open download icon pop-up' button
  Then choose '3' button in download pop-up
  Then choose 'EPS' download icon type in download pop-up
  Then click 'Download in icon bar esp' button
  Then try push text 'Free Download'
  Then sleep '10' seconds
  Then check and delete '.eps' file by extension
  Then go to Main page

#Scenario: Download PDF 50 px
#Scenario: 12: Download PDF 50 px
  #Then click logo icon8
  #Then push link in navigation menu 'Icons'
  #Then click 'Open download icon pop-up' button
  #Then move mouse to 'right bar' element
  #Then choose '1' button in download pop-up
  #Then choose 'PDF' download icon type in download pop-up
  #Then click 'Download in icon bar' button
  #Then try push text 'Free Download'
  #Then sleep '30' seconds
  #Then check and delete '.pdf' file by extension
  #Then click logo icon8

#Scenario: Download PDF 100 px
#Scenario: 13: Download PDF 100 px
  #Then click logo icon8
  #Then push link in navigation menu 'Icons'
  #Then click 'Open download icon pop-up' button
  #Then choose '2' button in download pop-up
  #Then choose 'PDF' download icon type in download pop-up
  #Then click 'Download in icon bar' button
  #Then try push text 'Free Download'
  #Then sleep '30' seconds
  #Then check and delete '.pdf' file by extension
  #Then click logo icon8

#Scenario: Download PDF 500 px
#Scenario: 14: Download PDF 500 px
  #Then click logo icon8
  #Then push link in navigation menu 'Icons'
  #Then click 'Open download icon pop-up' button
  #Then choose '3' button in download pop-up
  #Then choose 'PDF' download icon type in download pop-up
  #Then click 'Download in icon bar' button
  #Then try push text 'Free Download'
  #Then sleep '30' seconds
  #Then check and delete '.pdf' file by extension
  #Then click logo icon8
