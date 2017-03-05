Feature: Open pages, login and assertions

Scenario: Choose spanish localisation
Scenario: 1: Choose spanish localisation
  Then click logo icon8
  Then click 'selectLanguage' button element
  Then push link 'Spanish'
  Then click logo icon8

Scenario: Terms and Conditions  
Scenario: 2: Open Terms and Conditions page and assert text
  Then click logo icon8
  Then push link 'Términos y condiciones'
  Then scroll to end of the page
  Then locate text 'Nuestro modelo de negocio'
  Then locate text 'Licencia gratuita'
  Then locate text 'Comprar la licencia completa'
  Then locate text 'Versión de escritorio'
  Then click logo icon8

Scenario: Privacy Policy
Scenario: 3: Open Privacy Policy page and assertion
  Then click logo icon8
  Then push link 'Política de privacidad'
  Then scroll to end of the page
  Then locate text 'Nuestro modelo de negocio'
  Then locate text 'Licencia gratuita'
  Then locate text 'Comprar la licencia completa'
  Then locate text 'Versión de escritorio'
  Then click logo icon8
  
Scenario: Free license
Scenario: 4: Open Free license page and assertion
  Then click logo icon8
  Then push link 'Iconos gratis'
  Then scroll to end of the page
  Then locate text 'Utiliza los iconos de forma'
  Then locate text '¿Por qué añadir un enlace?'
  Then locate text '¿Dónde poner el enlace?'
  Then locate text 'Páginas web'
  Then locate text 'Aplicaciones de escritorio'
  Then locate text 'Aplicaciones móviles'
  Then locate text 'Código abierto'
  Then click logo icon8


Scenario: Paid license
Scenario: 5: Open Paid license page and assertion
  Then click logo icon8
  Then push link 'Iconos de pago'
  Then scroll to end of the page
  Then locate text 'Pagando o de gratis'
  Then locate text 'Resumen de la licencia de pago'
  Then locate text 'Usos prohibidos para todas las licencias'
  Then locate text 'Se incluye'
  Then locate text 'Herramientas de edición integradas'
  Then locate text 'Aplicación Icons8 para Mac y Windows'
  Then locate image '//cdnd.icons8.com/download/images/features_video_27.02.png'
  Then click logo icon8

Scenario: Contact us
Scenario: 6: Open Contact us page and assertion
  Then click logo icon8
  Then push link 'Contáctanos'
  Then scroll to end of the page
  Then locate text 'Contact Icons8'
  Then locate text 'Talk to a Human'
  Then locate text 'Our support team consists'
  Then click logo icon8

Scenario: Apps Win / Mac
Scenario: 7: Open Application page and assertion
  Then click logo icon8
  Then push link 'Descargar'
  Then click 'icon8 app in download pop-up' button
  Then scroll to end of the page
  Then locate text 'Descarga todos nuestros iconos'
  Then locate text 'Otras opciones de descarga'
  Then locate text 'Características'
  Then locate text 'Todos los iconos que necesitas. '
  Then locate text 'Populares'
  Then locate text 'Ver todo'
  Then locate text 'Funciones para diseñadores de interfaces'
  Then locate text 'Un mismo estilo'
  Then locate text 'Vectores editables'
  Then locate text 'Cambia el color'
  Then locate text 'Actualizaciones diarias'
  Then locate text 'A la comunidad'
  Then click logo icon8

Scenario: Request icons
Scenario: 8: Open Request icons page and assertion
  Then click logo icon8
  Then push link 'Solicitar'
  Then scroll to end of the page
  Then locate text 'Solicitar iconos'
  Then locate text 'Ideas de tendencia'
  Then locate text 'Últimas Ideas'
  Then locate text 'Ideas populares'
  Then locate text 'Mira todas las ideas de iconos'
  Then locate text 'Iconos creados'
  Then push 'Fast for $50/icon' from tabs
  Then locate text '¿Es rápido? ¿Pero cuánto?'
  Then locate text '¿Cuánto cuesta?'
  Then locate text '¿Por dónde comienzo?'
  Then locate text 'Cualquier icono, sin restricciones. Hasta 20 iconos por día. 50$ por icono'
  Then push 'Lento (gratis)' from tabs
  Then locate text 'Iconos creados'
  Then click logo icon8


Scenario: Cosmic Pedro
Scenario: 9: Open Cosmic Pedro page and assertion
  Then click logo icon8
  Then button with text 'Labs'
  Then push link 'Cosmic Pedro'
  Then locate text 'Cosmic Pedro'
  Then locate text 'Search for icon. Add text. Share!'
  Then go to Main page

Scenario: We love SVG
Scenario: 10: Open We love SVG page and assertion
  Then click logo icon8
  Then button with text 'Labs'
  Then push link 'We Love SVG'
  Then scroll to end of the page
  Then locate text 'Flat Color'
  Then push link 'Hello World!'
  Then locate text 'Simple jQuery Example'
  Then locate text '!DOCTYPE html'
  Then close popup
  Then back to previous page
  Then click logo icon8

Scenario: Web app
Scenario: 11: Open Web app page and assertion
  Then click logo icon8
  Then click 'selectLanguage' button element
  Then push link 'Spanish'
  Then click logo icon8
  Then push link in navigation menu 'Iconos'
  Then scroll to end of the page
  Then locate text 'Nuevos iconos'
  Then click logo icon8

Scenario: Logout feature
Scenario: 12: Logout and assertion
  Then click logo icon8
  Then locate text 'Mi cuenta'
  Then push link Logout
  Then push link 'Registrarse'
