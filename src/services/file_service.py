import json

from services.plan_service import PlanService


def export_plan_to_json(plan_service: PlanService, file_path: str):
    """Vie suunnitelman JSON-tiedostoon

    Args:
        plan_service (PlanService): Suunnitelmasta vastaava PlanService
        file_path (str): Vientitiedoston polku
    """

    study_plan_dict = plan_service.get_study_plan()

    json_object = json.dumps(study_plan_dict, indent=4)

    with open(file_path, "w", encoding="utf-8") as file:
        file.write(json_object)


def import_plan_from_json(plan_service: PlanService, file_path: str) -> bool:
    """Tuo suunnitelma JSON-tiedostosta

    Args:
        plan_service (PlanService): Suunnitelmasta vastaava PlanService
        file_path (str): Tuontitiedoston polku

    Returns:
        bool: Onnistuiko tuonti
    """
    with open(file_path, "r", encoding="utf-8") as file:
        import_json = file.read()

    import_dict = json.loads(import_json)

    import_meb_plan = import_dict["meb_plan"]
    new_meb_plan = {}

    for (period, subjects) in import_meb_plan.items():
        new_meb_plan[int(period)] = subjects

    import_dict["meb_plan"] = new_meb_plan

    return plan_service.import_study_plan(import_dict)
