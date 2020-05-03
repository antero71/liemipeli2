# liemipeli2
Uusi versio liemipelistä. Alunperin aloitin [liemipeli](https://github.com/antero71/liemipeli) -peliä javalla ja sitten muutin sen kotlin projektiksi, mutta 
se jäi enemmän vaiheeseen mitä tämä on nyt. Tämä peliversio perustuu vahvasti kirjan [Python Crash Course, 2nd Edition](https://nostarch.com/pythoncrashcourse2e) esimerkkiprojektiin
jossa opetellaan ohjelmoimaan "Alien invasion" -peli.

## Asennusohje

Asenna python 3.8 -versio koneellesi, jos sinulla 
ei ole sitä jo valmiiksi asennettuna.

## Windows

Microsoftin sivulta voi ladata ja asentaa [Python 3.8](https://www.microsoft.com/fi-fi/p/python-38/9mssztt1n39l?activetab=pivot:overviewtab) ohjelmiston.

Vaihtoehtoisesti asennuspaketin voi ladata [Pythonin sivulta](https://www.python.org/downloads/windows/)
Helpointa asennus on lataamalla 3.8.2 versio linkistä jossa lukee `Windows x86-64 executable installer` ja käynnistämällä asennus 
tuplaklikkaamalla exe-tiedostoa.

Kun python on asennettu, niin lataa peli koneellesi painamalla [sivun](https://github.com/antero71/liemipeli2) vihreää nappia, jossa 
lukee `clone or download`. Jos git-versiohallinta ei ole sinulle tuttu, niin paina `Download ZIP` valinnasta, jolloin selain
lataa zip-paketin koneellesi. Pura paketti sopivaan hakemistoon.
Avaa komentotulkki painamalla Windows-painiketta ja kirjoittamalla `cmd`
ja painamlla enter.

Siirry hakemistoon johon purit lataamasi zip -tiedoston. komennolla `cd c:\hakemisto\liemipeli-master\game`

Tässä hakemistossa pitää ensin antaa komento `pip install -r requirements.txt` joka asentaa pelissä käytetyn
[pygame](https://www.pygame.org/news) kirjaston koneellesi, jotta peli käynnistyy.
Tämän jälkeen peli käynnistetään komennolla `python wizards_broth.py`. Jos sinulla on ennestään vanhempi 
python 2 -versio koneellasi, saatat joutua antamaan komennon `python3 wizards_broth.py`, jotta peli käynnistyy.

Pythonin version saat selville antamalla komennon `python --version`.

Peli käynnistyy painamalla `p`.
Pelaajaa siirretään nuolinäppäimillä.
Peliohjeita saa näkyviin painamalla `o` ja ohjeet saa pois näkyvistä `esc` näppäimellä.
Peli lopetaan `q` -näppäintä painamalla.
Taskujen sisältö tarkistetaan `t` näppäimellä.

## Versionhallinta

Jos haluat harjoitella git-versionhallintaa, niin [git -clientin saa ladattua täältä](https://git-scm.com/downloads)
