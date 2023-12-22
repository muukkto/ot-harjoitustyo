# Opetussuunnitelma tiedoston rakenne

- **`rules`** *(objekti)*: *Ei saa sisältää ylimääräisiä tietoja.* Määrittää tuntijaon validioinnissa käytetyt säännöt.
  - **`minimum_credits`** *(kokonaisluku, pakollinen)* Vähimmäismäärä opintopisteitä kokonaisuudessaan (lops19 = 150).
  - **`minimum_national_voluntary_credits`** *(kokonaisluku, pakollinen)* Vähimmäismäärä valtakunnallisia valinnaisia opintopisteitä (lops19 = 20).
  - **`minimum_special_task_credits`** *(kokonaisluku, pakollinen)* Vähimmäismäärä erityistehtäväopintopisteitä poisluku oikeudne saavuttamiseksi (lops19 = 24).
  - **`maximum_excluded_credits_special_task`** *(kokonaisluku, pakollinen)* Enimäismäärä poisluettavia pakollisia opintopisteitä (lops19 = 16).
  - **`group_subjects`** *(lista, pakollinen)* Oppiaineryhmät joista riittää käydä yksi oppimäärä (esim. pitkä tai lyhyt matematiikka).
    - **Jäsenet** *(objekti)*: *Ei saa sisältää ylimääräisiä tietoja.* Yksi oppiaineryhmä.
      - **`name`** *(merkkijono, pakollinen)* Oppiaineryhmän nimi.
      - **`subjects`** *(lista, pakollinen)*: *Täytyy sisältää vähintään yhden jäsenen 1.* Oppiaineryhmään kuuluvat oppimäärät.
        - **Jäsenet** *(merkkijono)* Oppimäärän tunnus.
  - **`basket_subjects`** *(lista, pakollinen)* Oppiaineryhmät joista täytyy käydä kaikista oppiaineista minimimäärä opintopisteitä ja yhteensä toinen minimäärä opintopisteitä (esim. kuviksesta ja musiikista molemmista vähintään 2 op ja yhdessä vähintään 6 op).
    - **Jäsenet** *(objekti)*: *Ei saa sisältää ylimääräisiä tietoja.* Yksi oppiaineryhmä.
      - **`name`** *(merkkijono, pakollinen)* Oppiaineryhmän nimi.
      - **`subjects`** *(lista, pakollinen)*: *Täytyy sisältää vähintään yhden jäsenen 1.* Oppiaineryhmään kuuluvat oppimäärät.
        - **Jäsenet** *(merkkijono)* Oppimäärän tunnus.
      - **`minimum_compulsory_total`** *(kokonaisluku, pakollinen)* Yhteensä käytävä opintopisteiden minimimäärä.
      - **`minimum_compulsory_per_subject`** *(kokonaisluku, pakollinen)* Yksittäisten oppimäärien käytävä opintopisteiden minimimäärä.
  - **`national_mandatory_subjects`** *(lista, pakollinen)* Oppimäärät joista tarvitsee käydä jokaisesta kaikki pakolliset opintopisteet.
    - **Jäsenet** *(merkkijono)* Oppimäärän tunnus.
  - **`national_voluntary_subjects`** *(lista, pakollinen)* Oppimäärät joiden opintopisteet lasketaan mukaan valtakunnallisiin valinnaisiin opintopisteisiin.
    - **Jäsenet** *(merkkijono)* Oppimäärän tunnus.
  - **`special_task_code`** *(merkkijono)* Erityistehtäväkurssien tunnus. Tämän tunnuksen alaiset kurssit lasketaan erityistehtäväopintopisteiden määrään.
  - **`own_courses_codes`** *(lista)* Tunnukset jotka varattu koulukohtaisiin opintojaksoihin.
    - **Jäsenet** *(merkkijono)* Tunnuskoodi.
- **`subjects`** *(lista)* Opetussuunnitelmassa määritetyt oppimäärät ja kurssit.
  - **Jäsenet** *(objekti)* Yksi oppimäärä. 
    - **`name`** *(merkkijono)* Oppimäärän tunnus.
    - **`courses`** *(lista)* Oppimäärään kuuluvat kurssit.
      - **Jäsenet** *(objekti)* *Ei saa sisältää ylimääräisiä tietoja.*  Yksi kurssi.
        - **`name`** *(merkkijono)* Kurssin tunnus.
        - **`credits`** *(kokonaisluku)* Kurssin opintopistemäärä.
        - **`mandatory`** *(totuusarvo)* Tieto kurssin pakollisuudesta.
        - **`national`** *(totuusarvo)* Tieto kurssin valtakunnallisuudesta.



> [!WARNING]
> Ohjelma ei käynnisty, mikäli _curriculum.json_ ei noudata yllä olevaa skeemaa. 

> [!CAUTION]
> Opetussuunnitelma tiedoston täytyy vastata [uusimman lukion opetusuunnitelman perusteiden](https://eperusteet.opintopolku.fi/#/fi/lukiokoulutus/6828810/tiedot) mukaista tuntijakoa. Mikäli tiedoston tiedot poikkeavat lukion opetusuunnitelman perusteiden tuntijaosta, antaa opiskelusuunnitelman validiointi virheellisiä tuloksia. Pahimmassa tapauksessa validiointi hyväksyy virheelliset opiskelusuunnitelmat.
