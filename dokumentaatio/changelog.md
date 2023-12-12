# Changelog

## Viikko 3

- Perustietorakenteet pystyssä
    - Lisätty Course-luokka, joka vastaa käyttäjän merkinnöistä kursseihin - tällä hetkellä ainoa mahdollinen merkintä koskee kurssin kuulumista suunnitelmaan
    - Lisätty Plan-luokka vastaa käyttäjän opintosuunnitelmasta. Jokainen Plan-luokan instanssi luodaan Curriculumin avulla.
    - Lisätty Curriculum-luokka, jota tarvitaan suunnitelman validoinnissa.
- Tehty yksinkertainen config-opintosuunnitelma. Kaikki pakolliset oppiaineet löytyy jo siitä.
- Tehty erittäin yksinkertainen käyttöliittymä, joka voidaan suorittaa komennolla `poetry run invoke start`
    - Käyttöliittymästä ei löydy vielä minkäänlaista virheiden hallintaa tms.
- Lisätty PlanService-luokka jonka kautta suunnitelmaa voidaan muokata.
    - Pystytään lisäämään suunnitelman valtakunnallisia opintojaksoja
    - Pystytään poistamaan suunnitelmasta opintojaksoja
    - Vielä ei voi lisätä omia opintojaksoja
- Aloitettu validoinnin rakentamien
    - Mahdollisuus tarkistaa kokonaisopintopistemmärä
    - Mahdollisuus tarkistaa yksittäisen aineen pakolliset opintojaksot
    - Ei vielä mahdollista saada ihmisluettavaa palautetta
- Lisätty mahdollisuus lukea txt-tiedostosta opintojaksoja - tämä toiminnallisuus tarkoitettu lähinnä kehityksen helpottamiseksi 
- Perutietorakenteille löytyy testit. Voidaan suorittaa `poetry run invoke test` ja testikattavuus saadan `poetry run invoke coverage-report`

## Viikko 4

- Validoinnin parantaminen
    - Mahdollisuus tarkistaa, että pakolliset suoritettu kaikissa oppiaineissa. Ottaa huomioon mahdolliset eri oppimäärät ja taideaineiden poikkeavuudet.
    - Validiointi tarkistaa myös valtakunnalliset valinnaiset opinnot
    - Validointi mahdollista erityistehtävä-opintosuunnitelmalle
- Lisätty testit PlanService-luokalle sekä validoinneille.
- Luotu testit ValidationService-luokalle.
- Perustietorakenteet tukevat omia opintojaksoja

## Viikko 5

- Omat opintojaksot toimivat tekstikäyttöliittymässä ja PlanServicessä.
- Ylioppilastutkintosuunnitelma toimii. Luotu myös testit tälle.
- Ensimmäinen versio graafisesta käyttöliittymästä. Opintosuunnitelmaan kuuluvat kurssit on mahdollista valita ja tarkistaa. 
- Ylppärisuunnitelmaa pystyy muokkamaan ja tarkistamaan graafisessa käyttöliittymässä.
- Mahdollisuus tallentaa ja lukea suunnitelma JSON tiedostoon/tiedostosta. Vienti ja tuonti toimivat graafisen käyttöliittymän avulla.
- Suunnitelman voi vaihtaa eiryistehtäväksi ja takaisin graaffisessa käyttöliittymässä.

## Viikko 6

- Omia kursseja voi lisätä ja poistaa graafisesta käyttöliittymästä.
- Suunnitelma tallentuu tietokantaan.
- Tietokannassa voi olla monen käyttäjän suunnitelmat.
- Ohjelma hakee konfiguraatioita env-tiedostosta.
- Opetussuunnitelma haetaan JSON-tiedostosta