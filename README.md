*Helsingin yliopiston ohjelmistotekniikan kurssin (2023S) harjoitustyö*

# Study plan recorder & validator

Ohjelma joka pitää kirjaa lukion opintosuunnitelmasta ja tarkistaa riittääkö suunnitellut opinnot valmistumiseen.

## Dokumentaatio

- [Vaatimusmäärittely](dokumentaatio/vaatimusmaarittely.md)
- [Työaikakirjanpito](dokumentaatio/tuntikirjanpito.md)
- [Changelog](dokumentaatio\changelog.md)

## Komentorivikomennot

### Ohjelman suorittaminen
```
poetry run invoke start
```

### Ohjelman testaaminen
```
poetry run invoke test
```

### Testikattavuusraportti
```
poetry run invoke coverage-report
```