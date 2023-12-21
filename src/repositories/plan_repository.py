from database_connection import connection

from objects.course import Course


def return_plan(username: str) -> dict:
    """Palauttaa suunnitelman tietokannasta

    Args:
        username (str): Suunnitelman käyttäjänimi

    Returns:
        dict: Suunnitelma dict-objektina
    """
    db = connection

    return db[username]


def find_user(username: str) -> bool:
    """Tarkistaa löytyykö käyttäjätunnus jo tietokannasta

    Args:
        username (str): Kysytty käyttäjätunnus

    Returns:
        bool: Kyselyn tulos
    """
    if username in connection.keys():
        return True

    return False


def create_user(username: str) -> str:
    """Luo uuden käyttäjän

    Args:
        username (str): Uuden käyttäjän tunnus

    Returns:
        str: Tietokantaan tallennettu käyttäjätunnus
    """
    db = connection

    db[username] = {}

    db.commit()

    return username


def save_full_plan(username: str, plan_dict: dict):
    """Tallentaa koko suunnitelman tietokantaan

    Args:
        username (str): Käyttäjätunnus jonka alle suunnitelma tallennetaan
        plan_dict (dict): Tallennettava suunnitelma
    """
    db = connection

    db[username] = plan_dict

    db.commit()


def add_course(username: str, course: Course):
    """Lisää yhden kurssin tietokantaan

    Args:
        username (str): Käyttäjätunnus jonka alle kurssi tallennetaan
        course (Course): Kurssin tiedot
    """
    db = connection

    users_plan = db[username]

    list_courses = users_plan["courses"]

    list_courses.append(course.to_json())

    users_plan["courses"] = list_courses
    db[username] = users_plan

    db.commit()


def delete_course(username: str, code: str):
    """Poistaa kurssin tietokannasta

    Args:
        username (str): Käyttäjä jonka suunnitelmasta kurssi poistetaan
        code (str): Poistettavan kurssin koodi
    """
    db = connection

    users_plan = db[username]

    old_courses = users_plan["courses"]
    new_courses = []

    for old_course in old_courses:
        if not old_course["code"] == code:
            new_courses.append(old_course)

    users_plan["courses"] = new_courses
    db[username] = users_plan

    db.commit()


def add_meb_exam(username: str, exam_code: str, exam_period: int):
    """Lisää YO-kokeen tietokantaan

    Args:
        username (str): Käyttäjätunnus jonka alle koe lisätään
        exam_code (str): Lisättävän kokeen koodi
        exam_period (int): Lisättävän kokeen koeperiodi
    """
    db = connection

    users_plan = db[username]
    meb_plan = users_plan["meb_plan"]

    modified_period = meb_plan[exam_period]
    modified_period.append(exam_code)
    meb_plan[exam_period] = modified_period

    users_plan["meb_plan"] = meb_plan
    db[username] = users_plan

    db.commit()


def delete_meb_exam(username: str, exam_code: str, exam_period: int):
    """Poistaa YO-kokeen tietokannasta

    Args:
        username (str): Käyttäjätunnus jonka alta koe poistetaan
        exam_code (str): Poistettavan kokeen koodi
        exam_period (int): Poistettavan kokeen koeperiodi
    """
    db = connection

    users_plan = db[username]
    meb_plan = users_plan["meb_plan"]

    modified_period = meb_plan[exam_period]
    modified_period.remove(exam_code)
    meb_plan[exam_period] = modified_period

    users_plan["meb_plan"] = meb_plan
    db[username] = users_plan

    db.commit()


def change_config(username: str, new_config: dict):
    """Päivitetään suunnitelman konffaustiedot tietokantaan

    Args:
        username (str): Käyttäjätunnus jonka tietoja muutetaan
        new_config (dict): Uudet tiedot dict-objektina
    """
    db = connection

    users_plan = db[username]
    users_plan["config"] = new_config

    db[username] = users_plan

    db.commit()
