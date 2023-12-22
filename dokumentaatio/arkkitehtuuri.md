# Arkkitehtuurikuvaus

## Rakenne

Ohjelman rakenne on alla olevan kaavion mukainen:
```mermaid
graph TB
    db[(sqlite)]
    files[(files)]

    subgraph ui
    end

    subgraph services
        subgraph validation
            validationservice[ValidationService]
            mebvalidation[MEBValidationService]
            validationfunctions[ValidationFunctions]
            specialvalidationservice[SpecialValidationService]
        end
        planservice[PlanService]
        userservice[UserService]
        fileservice[FileService]
    end

    subgraph objects
        plan[Plan]
        curriculum[Curriculum]
        course[Course]
        user[User]
    end

    subgraph repositories
        planrepository[PlanRepository]
    end

    ui --> services
    services --> objects
    services --> repositories
    repositories --> db
    services --> files
    
```

Käyttöliittymä (_UI_) käyttää tietorakenteita (_Objects_) palveluiden (_Services_) kautta. _Services_ hoitaa siis kaikki sovelluslogiikan tehtävät. Tietokantaoperaatiot toteutetaan _repositories_-luokkien kautta. Tiedostoon kirjoittamiselle on oma _FileService_.


## Käyttöliittymä

Graafisessa käyttöliittymässä on kolme eri päänäkymää:

- Kirjautuminen
- Uuden käyttäjän luonti
- Suunnitelman päänäkymä

Edellä mainituista päänäkymistä ainoastaan yksi on kerrallaan esillä. Suunnitelman päänäkymästä on mahdollista avata pop-up ikkunoita. Jokainen pop-up ikkuna hoitaa oman pienen tehtävän. 

Päänäkymien luomisesta ja hallinnoinnista vastaa [UI](/src/ui/gui/ui.py)-luokka. Päänäkymät löytyvät [_views_](/src/ui/gui/views/)-kansiosta. Suunnitelman päänäkymä muodostuu pienistä [komponenteista](/src/ui/gui/components/). Jokainen komponentti vastaa yhdestä päänäkymän tarjoamasta toiminnallisuudesta. Jokainen komponentti toimii oman "framen" sisällä.

Kun käyttäjä kirjautuu sisälle latautuu tietokannasta aikaisempi versio käyttäjän suunnitelmasta. Näin ollen suunnitelman päänäkymään voidaan esimekiksi LOPS-puuhun valita jo valmiiksi aikaisemmin suunnitellut kurssit.

Käyttöliittymä ei vastaa sovelluslogiikasta. Käyttöliittymä muuttaa esimerkiksi suunnitelmaa [PlanServicen](/src/services/plan_service.py) tarjoamilla metodeilla. Käyttäjänhallinta hoituu puolestaan [UserServicen](/src/services/user_service.py) metodeilla.

Käyttöliittymä tekee kuitenkin eräitä validiointeja. Esimerkiksi käyttöliittymä mahdollistaa ainoastaan yhden YO-aineen valitsemisen samalla kirjoituspäivälle.

## Suunnitelman sovelluslogiikka

### Perustietorakenteet

Opiskelusuunnitelman tietorakenteet muodostaa kolme luokkaa: [Plan](/src/objects/plan.py), [Curriculum](/src/objects/curriculum.py) ja [Course](/src/objects/course.py).

```mermaid
classDiagram
    class Course {
        str code
        str subject
        str name
        int ects
        bool on_plan
        bool on_cur
        changeStatus(new_status)
        get_status() bool
        get_ects() int
        get_code() str
        to_json() dict
    }

    class Plan {
        dict cur_courses
        list own_courses
        bool special_task
        str username
        dict meb_plan
        str meb_language
        add_curriculum_course_to_plan(code) Course
        add_own_course_to_plan(code, name, credits) Course
        delete_course_from_plan(code) bool
        check_if_course_on_plan(code) bool
        get_courses_on_plan() list
        get_own_courses_on_plan() list
        get_credits_by_criteria(mandatory, national, subject_code) int
        get_credits_own_course() int
        get_total_credits_on_plan() int
        is_special_task() bool
        change_special_task(new_status)
        add_exam_to_meb_plan(exam_code, examination_period) bool
        remove_exam_from_meb_plan(exam_code, examination_period) bool
        get_curriculum_tree() dict
        return_study_plan() dict
        return_meb_plan() dict
        return_meb_language() str
        import_study_plan(study_plan) bool
    }

    class Curriculum {
        dict rules
        dict subjects
        return_all_subject_codes() list
        get_subject_code_from_course_code(course_code) str
        get_course_from_course_code(course_code) Course
        get_credits_from_course_code(course_code) int
        get_course_status_from_course_code(course_code) dict
        get_mandatory_credits_subject(subject_code) int
        return_all_courses_dict() dict
        return_rules() dict
    }

    Curriculum <-- Plan
    Curriculum .. Course
    Plan "1" --> "*" Course

```

Jokainen opiskelusuunnitelma (_Plan_) luodaan yhden opetussuunnitelman (_Curriculum_) pohjalta. _Plan_-luokan konstruktori lataa kaikki opetussuunnitelman kurssit suorittamattomiksi. _Plan_-luokka huolehtii suunnitelman tietojen tallentamisesta. Näitä on esimerkiksi kurssien suoritusteidot, YO-suunnitelma ja konfigurointitiedot.
Kurssitietoja varten on _Course_-luokka. Se vastaa kaikilla kursseilla tiedosta onko kurssi osa suunnitelmaa. Käyttäjän omilla kursseilla se myös vastaa kurssin nimestä ja opintopistemäärästä.

Opetussuunnitelma vastaa siihen kuuluvien kurssien tiedoista, kuten pakollisuus, opintopistemäärä ja oppiaine. Käyttäjän omien kurssien tapauksessa tämä tehtävä on _Course_-luokalla.

### Opintosuunnitelman hallinta

[PlanService](/src/services/plan_service.py) vastaa opintosuunnitelman hallinnasta. 

```mermaid
classDiagram
    class Plan {
        dict cur_courses
        list own_courses
        bool special_task
        str username
        dict meb_plan
        str meb_language
        add_curriculum_course_to_plan(code) Course
        add_own_course_to_plan(code, name, credits) Course
        delete_course_from_plan(code) bool
        check_if_course_on_plan(code) bool
        get_courses_on_plan() list
        get_own_courses_on_plan() list
        get_credits_by_criteria(mandatory, national, subject_code) int
        get_credits_own_course() int
        get_total_credits_on_plan() int
        is_special_task() bool
        change_special_task(new_status)
        add_exam_to_meb_plan(exam_code, examination_period) bool
        remove_exam_from_meb_plan(exam_code, examination_period) bool
        get_curriculum_tree() dict
        return_study_plan() dict
        return_meb_plan() dict
        return_meb_language() str
        import_study_plan(study_plan) bool
    }

    class PlanRepository {
        return_plan(username) dict
        find_user(username) bool
        create_user(username) str
        save_full_plan(username, plan)
        add_course(username, course)
        delete_course(username, code)
        add_meb_exam(username, exam_code, exam_period)
        delete_meb_exam(username, exam_code, exam_period)
        change_special_task(username, new_status)
    }

    class FileService {
        export_plan_to_json(study_plan, file_path)
        import_plan_from_json(file_path) dict
    }

    class Curriculum {
        dict rules
        dict subjects
        return_all_subject_codes() list
        get_subject_code_from_course_code(course_code) str
        get_course_from_course_code(course_code) Course
        get_credits_from_course_code(course_code) int
        get_course_status_from_course_code(course_code) dict
        get_mandatory_credits_subject(subject_code) int
        return_all_courses_dict() dict
        return_rules() dict
    }

    class UI {

    }

    class UserService {
        User user
        login(username) bool
        logout()
        create_user(username) bool
        get_current_username() str
    }

    class PlanService {
        Curriculum curriculum
        Plan plan
        UserService user_service
        create_empty_plan_for_user()
        read_plan_for_user()
        add_course(course_code, name, credits, in_cur) bool
        delete_course(course_code) bool
        get_curriculum_tree() -> dict
        get_course_status() -> bool
        get_stats() dict
        check_reserved_codes(course_code) bool
        validate_plan() list
        get_course_codes() list
        get_own_courses() list
        add_exam_meb(exam_code, exam_period) bool
        remove_exam_meb(exam_code, exam_period) bool
        validate_meb() dict
        get_study_plan() dict
        import_study_plan(study_plan_dict) bool
        get_meb_plan() dict
        change_special_task_status(new_status)
        get_config() dict
    }

    class ValidationService {
        validate() list
    }

    class MEBValidationService {
        validate() dict
    }

    Curriculum <-- Plan
    PlanService --> Plan
    PlanService --> Curriculum
    UserService .. Plan
    PlanService --> UserService
    PlanService --> ValidationService
    PlanService --> MEBValidationService
    PlanService .. PlanRepository
    PlanService .. FileService 
    ValidationService .. Plan
    ValidationService .. Curriculum
    MEBValidationService .. Plan
    UI --> PlanService
    UI --> UserService
```

_PlanService_-luokalla on tallennettuna viittaus yhteen _Plan_-objektiin. Tämä objekti joko luodaan `create_empty_plan_for_user`-funktiolla tai ladataan tietokannasta `read_plan_for_user`-funktiolla. Kaikki suunnitelmaa muuttavat funktio vaativat, että käyttäjä on kirjautuneena sisälle. _PlanService_ tarkistaa tämän _UserService_:ltä. 

_PlanService_ muokkaa suunnitelmaa _Plan_-objektin tarjoamilla funktioilla. _PlanService_ tekee tässä välissä muutamia validiointeja. _PlanService_ palauttaa myös tilastoja ja tietoja suunnitelmasta. _PlanServicen_ kautta tapahtuu myös suunnitelman validiointi.

### Suunnitelman tallentaminen tiedostoon tai tietokantaan

Jokaisella suunnitelman muokkauskutsulla _PlanService_ tekee kaksi asiaa: välittää tehtävän _Plan_-objektille ja mikäli muokkaus onnistuu, tekee vastaavan kutsun [PlanRepository](/src/repositories/plan_repository.py)-luokalle. _PlanRepository_-luokka huolehtii suunnitelman tallentamisesta tietokantaan. Tallentaminen tapahtuu `sqlitedict` moduulilla. Tämä moduuli antaa työkalut muokata _sqlite_-tietokantaa samoilla komennoilla kuin pythonin _dict_-objektia.

_PlanRepository_-luokka tarjoaa myös mahdollisuuden ladata kokosuunnitelman tietokannasta. Tätä käytetää _PlanServicen_ funktion `read_plan_for_user` yhteydessä. Tietokannan alustaminen tapahtuu invoke tehtävällä.

Suunnitelman voi tallentaa myös JSON-tiedostoon. Tämän hoitaa [FileService](/src/services/file_service.py)-luokka. Tiedostoon tallentaminen tapahtuu vain käyttäjän toiveesta, joten siitä vastaa eri luokka.

## Validioinnin sovelluslogiikka

Sovelluksessa on kaksi erilaista validiointia. Opiskelusuunnitelman validioinnista vastaa [ValidationService](/src/services/validation/validation_service.py). YO-suunnitelman validioinnille on oma [MEBValidationService](/src/services/validation/meb_validation_service.py).

### Opiskelusuunnitelman validiointi

Opiskelusuunnitelman validiointia varten _ValidationService_-luokka tarjoaa funktion `validate`. Funktio ottaa argumenteiksi _Plan_ ja _Curriculum_ -objektit. Validioinnin säännöt saadaan _Curriculum_ -objektista. _Plan_-objekti palauttaa puolestaan validioinnin vaatimat tiedot opintopisteistä ja suunnitelman konfiguraatiosta.

Validiointi tarkistaa seuraavat asiat:
- Suunnitelmalla on yhteensä tarpeeksi opintopisteitä
- Suunnitelmalla on tarpeeksi valtakunnallisia valinnaisia opintopisteitä
- Suunnitelmaan kuuluu kaikki pakolliset opintopisteet (tämän toiminnallisuuden yksityiskohdat riippuvat suunnitelman tyypistä)

Suunnitelmalla on kaksi mahdollista tyyppiä: normaali suunnitelma ja erityistehtäväsuunnitelma. Erityistehtäväsuunnitelmaa varten pakollisten opintopisteiden tarkastaminen tehdään luokan [SpecialValidationService](/src/services/validation/special_validation_service.py) kautta. Tämä luokka tarkistaa ensiksi, että löytyykö tarpeeksi erityistehtäväopintopisteitä, jotta poislukuoikeus voidaan ansaita. Tämän jälkeen pakolliset opintopisteet tarkistetaan seuraavilla ehdoilla:
- Jokaisesta oppiaineesta täytyy suorittaa vähintään puolet pakollisista opintopisteistä.
- Yhteensä puuttuvia pakollisia opintopisteitä saa olla opetusuunnitelman säännön `maximum_excluded_credits_special_task` määrittämä määrä. 

Normaalin suunnitelman pakolliset opintopisteet tarkistetaan luokan _ValidationService_-toimesta. Molemmat tavat hyödyntävät luokan [ValidationFunctions](/src/services/validation/validation_functions.py) funktioita pakollisten opintopisteiden laskemiseen. 

Lopuksi _ValidationService_ palauttaa validoinnin tulokset _dict_-objektina. Käyttöliittymä tulostaa tulokset ihmisluettavassa muodossa.

```mermaid
sequenceDiagram
actor User
participant UI
User ->> UI: click "validate plan" button

participant PlanService
UI ->> PlanService: validate_plan()
participant ValidationService
PlanService ->> ValidationService: validate(plan, curriculum)

participant Curriculum
participant Plan
ValidationService ->> Curriculum: return_rules()
Curriculum --> ValidationService: return rules_dict 
ValidationService ->> Plan: get_total_credits_on_plan()
Plan --> ValidationService: return total_credits
ValidationService ->> Plan: get_credits_by_criteria(mandatory=False,national=True)
Plan --> ValidationService: return credits

ValidationService ->> Plan: return_config()
Plan --> ValidationService: return config_dict

alt if config_dict["special_task"]
    participant SpecialValidationService
    ValidationService ->> SpecialValidationService: validate(plan, curriculum)

    SpecialValidationService ->> Curriculum: return_rules()
    Curriculum --> SpecialValidationService: return rules_dict 
    SpecialValidationService ->> Plan: get_credits_by_criteria(mandatory=False, national=False, subject="ERI")
    Plan --> SpecialValidationService: return credits

    participant ValidationFunctions
    SpecialValidationService ->> ValidationFunctions: check_total_mandatory(plan, curriculum, problem_list)
    loop all subjects
        ValidationFunctions ->> Plan: get_mandatory_credits_subject(subject)
        Plan --> ValidationFunctions: return credits
    end

    ValidationFunctions --> SpecialValidationService: return excluded_credits
    SpecialValidationService --> ValidationService: return validation_problems

else
    participant ValidationFunctions
    ValidationService ->> ValidationFunctions: check_total_mandatory(plan, curriculum, problem_list)

    loop all subjects
        ValidationFunctions ->> Plan: get_mandatory_credits_subject(subject)
        Plan --> ValidationFunctions: return credits
    end

    ValidationFunctions --> ValidationService: return excluded_credits

end

ValidationService --> PlanService: return validation_problems
PlanService --> UI: return validation_problems
UI --> User: open validation result as pop-up

```

### YO-suunnitelman validiointi

YO-suunnitelma validioidaan _MebValidationService_ luokan `validate`-funktiolla. Funktio tekee kaksi erilaista tarkistusta:
- Funktio tarkistaa paikallisesti, että suunnitelmalle ei ole valittu kahta tai useampaa koetta samalle koepäivälle.
- Tutkinnon rakenne tarkistetaan Ylioppilastutkintolautakunnan [palvelun](https://ilmo.ylioppilastutkinto.fi/v1/api-docs/) avulla.

Validoinnin tulokset palautetaan _dict_-objektina. Käyttöliittymä tulostaa tulokset ihmisluettavassa muodossa.

```mermaid
sequenceDiagram
actor User
participant UI
User ->> UI: click "validate MEB plan" button

participant PlanService
UI ->> PlanService: validate_meb_plan()
participant MebValidationService
PlanService ->> MebValidationService: validate(plan)

participant Plan
MebValidationService ->> Plan: return_meb_plan()
Plan --> MebValidationService: return meb_plan_dict

participant MEB api service (internet)
MebValidationService ->> MEB api service (internet): request
MEB api service (internet) --> MebValidationService: reponse

MebValidationService --> PlanService: return validation_result
PlanService --> UI: return validation_result
UI --> User: open validation result as pop-up

```