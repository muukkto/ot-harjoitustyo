*Helsingin yliopiston ohjelmistotekniikan kurssin (2023S) harjoitustyö*

# Study plan recorder & validator

Ohjelma joka pitää kirjaa lukion opintosuunnitelmasta ja tarkistaa riittääkö suunnitellut opinnot valmistumiseen.

## Julkaisut

[Viikon 5 julkaisu](https://github.com/muukkto/ot-harjoitustyo/releases/viikko5)

## Dokumentaatio

- [Vaatimusmäärittely](dokumentaatio/vaatimusmaarittely.md)
- [Työaikakirjanpito](dokumentaatio/tuntikirjanpito.md)
- [Changelog](dokumentaatio/changelog.md)
- [Arkkitehtuuri](dokumentaatio/arkkitehtuuri.md)

## Asennus
1. Riipuvuudet täytyy asentaa komennolla:
```
poetry install
```

2. Graafisen käyttöliittymän saa käynnistettyä komennolla:
```
poetry run invoke start
```

## Komentorivikomennot

### Ohjelman suorittaminen
Graafinen käyttöliittymä
```
poetry run invoke start
```

Tekstikäyttöliittymä (ei välttämättä toimi)
```
poetry run invoke start-text
```


### Ohjelman testaaminen
```
poetry run invoke test
```

### Testikattavuusraportti
```
poetry run invoke coverage-report
```

### Koodin laaduun analyysi
```
poetry run invoke lint
```
