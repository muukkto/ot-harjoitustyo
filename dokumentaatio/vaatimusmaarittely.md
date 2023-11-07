# Vaatimusmäärittely

## Sovelluksen kuvaus

Ohjelmaan pystyy kirjaamaan oman lukion opintosuunnitelman. Ohjelma tarkistaa riittääkö suunnitelman opinnot valmistumiseen. 

## Perustoiminnallisuudet

- [ ] Opintojaksojen merkitseminen suunnitelmaan kuuluvaksi. Toteutetaan ensiksi komentoriviltä, esim `add MAA12`.
- [ ] Opintojakson poistaminen suunnitelmasta - `delete MAA12`
- [ ] Suunnitelmaan voi lisätä oppilaitoskohtaisia valinnaisia opintojaksoja - täytyy itse antaa nimi ja opintopistemäärä
- [ ] Suunnitelman tarkastaminen (perus)
    - [ ] Valmistua voi pelkästään kun 150 op kasassa
    - [ ] Kaikki pakolliset opintojaksot täytyy käydä
    - [ ] Vähintää 20 op valtakunnallisia valinnaisia
- [ ] Ylppärisuunnitelman tarkistaminen
    - [ ] Suunnitelma tarkistetaan YTL:n palvelusta. [Linkki API:n dokumentaatioon](https://ilmo.ylioppilastutkinto.fi/v1/api-docs/).
    - [ ] Ei päälekkäisiä kokeita suunnitelmassa (esim. reaalit samana päivänä) - tämä tehdään paikallisesti
- [ ] Suunnitelman tarkastaminen (erityistehtävä)
    - [ ] Pakollisia voi jättää pois 16 op, jos erityistehtävä opintojaksoja on 24 op
    - [ ] Puolet pakollisista kuitenkin käytävä
- [ ] Yksinkertainen tekstikäyttöliittymä
- [ ] Suunnitelman tallentaminen JSON-tiedostoon
- [ ] Suunnitelman lukeminen JSON-tiedostosta
- [ ] Mahdollisuus tulostaa perustilastoja
    - [ ] Opintojaksojen kokonaismäärä
    - [ ] Pakollisten määrä
    - [ ] Valinnaisten määrä


## Jatkokehitysideat

- [ ] Ohjelmaa pystyy käyttämään moni käyttäjä - alussa valitaan käyttäjätunnuksen perusteella oma suunnitelma
- [ ] Graafinen käyttöliittymä
    - [ ] Opintojaksot voidaan kliksutella LOPS-puusta
- [ ] LOPS-puu voidaan ladata JSON-tiedostosta
    - [ ] Mahdollisuus oppilaitoskohtaisiin valinnaisiin opintojaksoihin
- [ ] Ehdotukset mitä puuttuu valmistumisesta, esim `pakollisista puuttuu ENA6, BI2, BI3 ...`
- [ ] Opintojakson yhteyteen voidaan valita suoritusaika
- [ ] Edistyneet tilastot
    - [ ] Vuosittainen opintopistemäärä
- [ ] Tietojen tallentaminen tietokantaan


## Edistyneitä jatkokehitysiedoita

- [ ] Ylläpito-oikeudet
    - [ ] LOPS-puun muokkaaminen vaatii ylläpito-oikeudet
    - [ ] Valmistumiskriitereiden muuttaminen käyttöliittymästä - esim. aikuislukiot