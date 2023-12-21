# Testausdokumentti

Sovelluslogiikan testaus on hoidettu automatisoiduin yksikkö- ja integraatiotestein hyödyntäen Pythonin `unittest`-kirjastoa. Käyttöliittymä ja tiedostojen tallennus on testattu manuaalisesti.

## Yksikkö- ja integraatiotestaus


## Manuaaliset testit


## Sovelluksen ongelmat

- Sovelluksen konfiguraation oikeudenmukaisuudella on kevyet testit. Kaikkia poikkeustapauksia ei ole ehditty huomioimaan/testaamaan. Varminta on suorittaa ohjelmaa valmiiksi tehdyillä konfiguraatiotiedostoilla (nämä tiedostot ovat myös Ylioppilastutkintolautakunnan määräysten ja lukion opetussuunnitelman perusteiden 2019 mukaiset). 
- Graafisessa käyttöliittymässä voi olla välillä ongelmia objektien sijoittumisen kanssa. Esim. YO-suunnitelmaa muokatessa puolet vaihtoehdoista jäävät avautuvan ikkunan ulkopuolelle.