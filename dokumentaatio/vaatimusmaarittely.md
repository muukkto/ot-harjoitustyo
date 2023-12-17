# Vaatimusmäärittely

## Sovelluksen kuvaus

Ohjelmaan pystyy kirjaamaan oman lukion opintosuunnitelman. Ohjelma tarkistaa riittääkö suunnitelman opinnot valmistumiseen. 

## Perustoiminnallisuudet

- [x] Opintojaksojen merkitseminen suunnitelmaan kuuluvaksi. Toteutetaan ensiksi komentoriviltä, esim `add MAA12`.
- [x] Opintojakson poistaminen suunnitelmasta - `delete MAA12`
- [x] Suunnitelmaan voi lisätä oppilaitoskohtaisia valinnaisia opintojaksoja - täytyy itse antaa nimi ja opintopistemäärä
- [x] Suunnitelman tarkastaminen (perus)
    - [x] Valmistua voi pelkästään kun 150 op kasassa
    - [x] Kaikki pakolliset opintojaksot täytyy käydä
    - [x] Vähintää 20 op valtakunnallisia valinnaisia
- [x] Ylppärisuunnitelman tarkistaminen
    - [x] Ylppärisuunnitelman laatiminen    
    - [x] Suunnitelma tarkistetaan YTL:n palvelusta. [Linkki API:n dokumentaatioon](https://ilmo.ylioppilastutkinto.fi/v1/api-docs/).
    - [x] Ei päälekkäisiä kokeita suunnitelmassa (esim. reaalit samana päivänä) - tämä tehdään paikallisesti
- [x] Suunnitelman tarkastaminen (erityistehtävä)
    - [x] Pakollisia voi jättää pois 16 op, jos erityistehtävä opintojaksoja on 24 op
    - [x] Puolet pakollisista kuitenkin käytävä
- [x] Yksinkertainen tekstikäyttöliittymä
- [x] Suunnitelman tallentaminen JSON-tiedostoon
- [x] Suunnitelman lukeminen JSON-tiedostosta
- [x] Mahdollisuus tulostaa perustilastoja
    - [x] Opintojaksojen kokonaismäärä
    - [x] Pakollisten määrä
    - [x] Valinnaisten määrä


## Jatkokehitysideat

- [x] Graafinen käyttöliittymä
    - [x] Opintojaksot voidaan kliksutella LOPS-puusta
    - [x] YO-suunnitelman aineet voidaan valita vetovalikosta.
    - [x] Validiointi tulostaa "kauniit" vastaukset 
    - [x] Oman opintojakson voi syöttää käyttöliittymästä. Se ilmestyy häntäkurssina.
- [x] LOPS-puu voidaan ladata JSON-tiedostosta
    - [x] Mahdollisuus oppilaitoskohtaisiin valinnaisiin opintojaksoihin
- [x] Validiointi kertoo missä aineissa on ongelmia
- [ ] Opintojakson yhteyteen voidaan valita suoritusaika
- [ ] Edistyneet tilastot
    - [ ] Vuosittainen opintopistemäärä
- [x] Tietojen tallentaminen tietokantaan
- [x] Ohjelmaa pystyy käyttämään moni käyttäjä - alussa valitaan käyttäjätunnuksen perusteella oma suunnitelma
- [x] Tietokanta polut ja muut konfiguroinnit saadaan tiedostosta
- [x] Suunnitelman konfiguraatioita voidaan muuttaa
    - [x] Noudattaako suunnitelma erityistehtän tuntijakoa
    - [x] YO-tutkinnon kieli
    - [x] Valmistumisajankohta (tällöin examination period 1 vaihtuu esim. 2024K jne.)
