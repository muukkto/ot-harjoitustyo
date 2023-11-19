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
