# pois pylint, koska tämä ainoastaan käytössä luodessa opetussuunnitelma kehitystä varten
# tulavisuudessa tämän funktion tehtävä siirretään json tiedostolle

# pylint: disable=line-too-long

def lops21_curriculum():
    lops21 = {
        "rules": {
            "minimum_credits": 150,
            "minimum_national_voluntary_credits": 20,
            "mother_tongue": ["AI", "S2"],
            "second_national_language": ["RUA", "RUB"],
            "long_foreign_language": ["ENA", "RAA", "SAA", "VEA"],
            "maths": ["MAA", "MAB"],
            "national_mandatory_subjects": ["BI", "GE", "FY", "KE", "PS", "FI", "HI", "YH", "TE", "LI", "OP"],
            "worldview": ["UE", "ET", "UO", "UK", "UI", "UJ"],
            "basket_subjects": {"arts": {"codes": ["KU", "MU"], "minimum_compulsory_total": 6, "minimum_compulsory_per_subject": 2}},
            "national_voluntary_subjects": ["EAB3", "RAB3", "SAB3", "VEB3", "LAB3", "IAB3", "KIB3", "JPB3"],
            "special_task_code": "ERI",
            "own_courses_codes": ["VAPA"]
        },
        "subjects": {
            "AI": {"courses": {"AI1": {"credits": 2, "mandatory": True, "national": True}, "AI2": {"credits": 1, "mandatory": True, "national": True}, "AI3": {"credits": 1, "mandatory": True, "national": True}, "AI4": {"credits": 2, "mandatory": True, "national": True}, "AI5": {"credits": 2, "mandatory": True, "national": True}, "AI6": {"credits": 1, "mandatory": True, "national": True}, "AI7": {"credits": 1, "mandatory": True, "national": True}, "AI8": {"credits": 2, "mandatory": True, "national": True}, "AI9": {"credits": 2, "mandatory": False, "national": True}, "AI10": {"credits": 2, "mandatory": False, "national": True}, "AI11": {"credits": 2, "mandatory": False, "national": True}}},
            "S2": {"courses": {"S21": {"credits": 2, "mandatory": True, "national": True}, "S22": {"credits": 1, "mandatory": True, "national": True}, "S23": {"credits": 1, "mandatory": True, "national": True}, "S24": {"credits": 2, "mandatory": True, "national": True}, "S25": {"credits": 2, "mandatory": True, "national": True}, "S26": {"credits": 1, "mandatory": True, "national": True}, "S27": {"credits": 1, "mandatory": True, "national": True}, "S28": {"credits": 2, "mandatory": True, "national": True}, "S29": {"credits": 2, "mandatory": False, "national": True}, "S210": {"credits": 2, "mandatory": False, "national": True}, "S211": {"credits": 2, "mandatory": False, "national": True}}},
            "RUA": {"courses": {"RUA1": {"credits": 1, "mandatory": True, "national": True}, "RUA2": {"credits": 3, "mandatory": True, "national": True}, "RUA3": {"credits": 2, "mandatory": True, "national": True}, "RUA4": {"credits": 2, "mandatory": True, "national": True}, "RUA5": {"credits": 2, "mandatory": True, "national": True}, "RUA6": {"credits": 2, "mandatory": True, "national": True}, "RUA7": {"credits": 2, "mandatory": False, "national": True}, "RUA8": {"credits": 2, "mandatory": False, "national": True}}},
            "RUB": {"courses": {"RUB1": {"credits": 1, "mandatory": True, "national": True}, "RUB2": {"credits": 3, "mandatory": True, "national": True}, "RUB3": {"credits": 2, "mandatory": True, "national": True}, "RUB4": {"credits": 2, "mandatory": True, "national": True}, "RUB5": {"credits": 2, "mandatory": True, "national": True}, "RUB6": {"credits": 2, "mandatory": False, "national": True}, "RUB7": {"credits": 2, "mandatory": False, "national": True}}},
            "ENA": {"courses": {"ENA1": {"credits": 1, "mandatory": True, "national": True}, "ENA2": {"credits": 3, "mandatory": True, "national": True}, "ENA3": {"credits": 2, "mandatory": True, "national": True}, "ENA4": {"credits": 2, "mandatory": True, "national": True}, "ENA5": {"credits": 2, "mandatory": True, "national": True}, "ENA6": {"credits": 2, "mandatory": True, "national": True}, "ENA7": {"credits": 2, "mandatory": False, "national": True}, "ENA8": {"credits": 2, "mandatory": False, "national": True}}},
            "RAB3": {"courses": {"RAB31": {"credits": 2, "mandatory": False, "national": True}, "RAB32": {"credits": 2, "mandatory": False, "national": True}, "RAB33": {"credits": 2, "mandatory": False, "national": True}, "RAB34": {"credits": 2, "mandatory": False, "national": True}, "RAB35": {"credits": 2, "mandatory": False, "national": True}, "RAB36": {"credits": 2, "mandatory": False, "national": True}, "RAB37": {"credits": 2, "mandatory": False, "national": True}, "RAB38": {"credits": 2, "mandatory": False, "national": True}}},
            "MAA": {"courses": {"MAA1": {"credits": 2, "mandatory": True, "national": True}, "MAA2": {"credits": 3, "mandatory": True, "national": True}, "MAA3": {"credits": 2, "mandatory": True, "national": True}, "MAA4": {"credits": 3, "mandatory": True, "national": True}, "MAA5": {"credits": 2, "mandatory": True, "national": True}, "MAA6": {"credits": 3, "mandatory": True, "national": True}, "MAA7": {"credits": 2, "mandatory": True, "national": True}, "MAA8": {"credits": 2, "mandatory": True, "national": True}, "MAA9": {"credits": 1, "mandatory": True, "national": True}, "MAA10": {"credits": 2, "mandatory": False, "national": True}, "MAA11": {"credits": 2, "mandatory": False, "national": True}, "MAA12": {"credits": 2, "mandatory": False, "national": True}}},
            "MAB": {"courses": {"MAB1": {"credits": 2, "mandatory": True, "national": True}, "MAB2": {"credits": 2, "mandatory": True, "national": True}, "MAB3": {"credits": 2, "mandatory": True, "national": True}, "MAB4": {"credits": 2, "mandatory": True, "national": True}, "MAB5": {"credits": 2, "mandatory": True, "national": True}, "MAB6": {"credits": 1, "mandatory": True, "national": True}, "MAB7": {"credits": 1, "mandatory": True, "national": True}, "MAB8": {"credits": 2, "mandatory": False, "national": True}, "MAB9": {"credits": 2, "mandatory": False, "national": True}}},
            "UE": {"courses": {"UE1": {"credits": 2, "mandatory": True, "national": True}, "UE2": {"credits": 2, "mandatory": True, "national": True}, "UE3": {"credits": 2, "mandatory": False, "national": True}, "UE4": {"credits": 2, "mandatory": False, "national": True}, "UE5": {"credits": 2, "mandatory": False, "national": True}, "UE6": {"credits": 2, "mandatory": False, "national": True}}},
            "ET": {"courses": {"ET1": {"credits": 2, "mandatory": True, "national": True}, "ET2": {"credits": 2, "mandatory": True, "national": True}, "ET3": {"credits": 2, "mandatory": False, "national": True}, "ET4": {"credits": 2, "mandatory": False, "national": True}, "ET5": {"credits": 2, "mandatory": False, "national": True}, "ET6": {"credits": 2, "mandatory": False, "national": True}}},
            "BI": {"courses": {"BI1": {"credits": 2, "mandatory": True, "national": True}, "BI2": {"credits": 1, "mandatory": True, "national": True}, "BI3": {"credits": 1, "mandatory": True, "national": True}, "BI4": {"credits": 2, "mandatory": False, "national": True}, "BI5": {"credits": 2, "mandatory": False, "national": True}, "BI6": {"credits": 2, "mandatory": False, "national": True}}},
            "GE": {"courses": {"GE1": {"credits": 2, "mandatory": True, "national": True}, "GE2": {"credits": 2, "mandatory": False, "national": True}, "GE3": {"credits": 2, "mandatory": False, "national": True}, "GE4": {"credits": 2, "mandatory": False, "national": True}}},
            "FY": {"courses": {"FY1": {"credits": 1, "mandatory": True, "national": True}, "FY2": {"credits": 1, "mandatory": True, "national": True}, "FY3": {"credits": 2, "mandatory": False, "national": True}, "FY4": {"credits": 2, "mandatory": False, "national": True}, "FY5": {"credits": 2, "mandatory": False, "national": True}, "FY6": {"credits": 2, "mandatory": False, "national": True}, "FY7": {"credits": 2, "mandatory": False, "national": True}, "FY8": {"credits": 2, "mandatory": False, "national": True}}},
            "KE": {"courses": {"KE1": {"credits": 1, "mandatory": True, "national": True}, "KE2": {"credits": 1, "mandatory": True, "national": True}, "KE3": {"credits": 2, "mandatory": False, "national": True}, "KE4": {"credits": 2, "mandatory": False, "national": True}, "KE5": {"credits": 2, "mandatory": False, "national": True}, "KE6": {"credits": 2, "mandatory": False, "national": True}}},
            "PS": {"courses": {"PS1": {"credits": 2, "mandatory": True, "national": True}, "PS2": {"credits": 2, "mandatory": False, "national": True}, "PS3": {"credits": 2, "mandatory": False, "national": True}, "PS4": {"credits": 2, "mandatory": False, "national": True}, "PS5": {"credits": 2, "mandatory": False, "national": True}}},
            "FI": {"courses": {"FI1": {"credits": 2, "mandatory": True, "national": True}, "FI2": {"credits": 2, "mandatory": True, "national": True}, "FI3": {"credits": 2, "mandatory": False, "national": True}, "FI4": {"credits": 2, "mandatory": False, "national": True}}},
            "HI": {"courses": {"HI1": {"credits": 2, "mandatory": True, "national": True}, "HI2": {"credits": 2, "mandatory": True, "national": True}, "HI3": {"credits": 2, "mandatory": True, "national": True}, "HI4": {"credits": 2, "mandatory": False, "national": True}, "HI5": {"credits": 2, "mandatory": False, "national": True}, "HI6": {"credits": 2, "mandatory": False, "national": True}}},
            "YH": {"courses": {"YH1": {"credits": 2, "mandatory": True, "national": True}, "YH2": {"credits": 2, "mandatory": True, "national": True}, "YH3": {"credits": 2, "mandatory": True, "national": True}, "YH4": {"credits": 2, "mandatory": False, "national": True}}},
            "TE": {"courses": {"TE1": {"credits": 2, "mandatory": True, "national": True}, "TE2": {"credits": 2, "mandatory": False, "national": True}, "TE3": {"credits": 2, "mandatory": False, "national": True}}},
            "LI": {"courses": {"LI1": {"credits": 2, "mandatory": True, "national": True}, "LI2": {"credits": 2, "mandatory": True, "national": True}, "LI3": {"credits": 2, "mandatory": False, "national": True}, "LI4": {"credits": 2, "mandatory": False, "national": True}, "LI5": {"credits": 2, "mandatory": False, "national": True}}},
            "OP": {"courses": {"OP1": {"credits": 2, "mandatory": True, "national": True}, "OP2": {"credits": 2, "mandatory": True, "national": True}}},
            "KU": {"courses": {"KU1": {"credits": 2, "mandatory": True, "national": True}, "KU2": {"credits": 2, "mandatory": True, "national": True}, "KU3": {"credits": 2, "mandatory": False, "national": True}, "KU4": {"credits": 2, "mandatory": False, "national": True}}},
            "MU": {"courses": {"MU1": {"credits": 2, "mandatory": True, "national": True}, "MU2": {"credits": 2, "mandatory": True, "national": True}, "MU3": {"credits": 2, "mandatory": False, "national": True}, "MU4": {"credits": 2, "mandatory": False, "national": True}}},
        }
    }

    return lops21


# pylint: disable=pointless-string-statement

"""
Ainekoodit:
AI = äidinkieli
S2 = suomi toisena kielenä

RUA = ruotsi A-oppimäärä
RUB = ruotsi B1-oppimäärä


VKA = geneerinen vieraskieli A-oppimäärä
ENA = englanti A-oppimäärä
RAA = ranska A-oppimäärä
SAA = saksa A-oppimäärä
VEA = venäjä A-oppimäärä 

VKB3 = geneerinen vieraskieli B3-oppimäärä
EAB3 = espanja B3-oppimäärä
RAB3 = ranska B3-oppimäärä
SAB3 = saksa B3-oppimäärä
VEB3 = venäjä B3-oppimäärä
LAB3 = latina B3-oppimäärä
IAB3 = italia B3-oppimäärä
KIB3 = kiina B3-oppimäärä
JPB3 = japani B3-oppimäärä


MAA = matematiikka pitkä oppimäärä
MAB = matematiikka lyhyt oppimäärä


BI = biologia
GE = maantiede
FY = fysiikka
KE = kemia
PS = psykologia
FI = filosofia
HI = historia
YH = yhteiskuntaoppi
TE = terveystieto

USK = geneerinen uskonto
ET = elämänkatsomustieto
UE = uskonto, ev.lut.
UO = uskonto, ortodoksi
UK = uskonto, katolinen
UI = uskonto, islam
UJ = uskonto, juutalaisuus

MU = musiikki
KU = kuvataide
LI = liikunta


OP = opinto-ohjaus


VAPA = vapaa-valintaiset
ERI = erityistehtäväkurssit
"""
