import json
from jsonschema import validate, ValidationError

from schemas.curriculum_schema import curriculum_schema
from schemas.plan_schema import plan_schema


def export_plan_to_json(study_plan: dict, file_path: str):
    """Vie suunnitelman JSON-tiedostoon

    Args:
        study_plan (dict): Opintosuunnitelma dict-objektina
        file_path (str): Vientitiedoston polku
    """

    json_object = json.dumps(study_plan, indent=4)

    with open(file_path, "w", encoding="utf-8") as file:
        file.write(json_object)


def import_plan_from_json(file_path: str) -> dict:
    """Tuo suunnitelma JSON-tiedostosta

    Funktio validioi että tuotavan tiedoston skeema on oikea. 
    Mikäli skeema ei ole oikea, palauttaa None.

    Args:
        file_path (str): Tuontitiedoston polku

    Returns:
        dict: Opintosuunnitelman dict-objekti
    """
    with open(file_path, "r", encoding="utf-8") as file:
        import_json = file.read()

    import_dict = json.loads(import_json)

    try:
        validate(instance=import_dict, schema=plan_schema)

    except ValidationError:
        return None

    import_meb_plan = import_dict["meb_plan"]
    new_meb_plan = {}

    for (period, subjects) in import_meb_plan.items():
        new_meb_plan[int(period)] = subjects

    import_dict["meb_plan"] = new_meb_plan

    return import_dict


def import_curriculum_from_json(file_path: str) -> dict:
    """Ladataan opetussuunnitelma tiedostosta.

    Funktio validioi että tuotavan tiedoston skeema on oikea. 
    Mikäli skeema ei ole oikea, palauttaa None.    

    Args:
        file_path (str): Tuontitiedoston polku

    Returns:
        dict: Opetussuunnitelma dict-objektina
    """
    with open(file_path, "r", encoding="utf-8") as file:
        import_json = file.read()

    import_cur = json.loads(import_json)

    try:
        validate(instance=import_cur, schema=curriculum_schema)
        return import_cur

    except ValidationError:
        return None
