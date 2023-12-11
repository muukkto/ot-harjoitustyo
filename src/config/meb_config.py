import csv
from pathlib import Path

dirname = Path(__file__).parent
file_path = dirname.joinpath("meb_course_codes.csv")


def get_meb_codes(language: str) -> list:
    with open(file_path, "r", encoding="utf-8") as meb_csv:
        data = csv.DictReader(meb_csv, delimiter=";")

        codes = []

        for col in data:
            if col["EXAM_LANGUAGE"] == language.upper() or col["EXAM_LANGUAGE"] == "BOTH":
                codes.append(col["KOODI"])

    return codes


def get_meb_names_and_codes_by_day(language: str):
    with open(file_path, "r", encoding="utf-8") as meb_csv:
        data = csv.DictReader(meb_csv, delimiter=";")

        calendar = {}

        for day in range(1, 9):
            calendar[day] = {"(none)": None}

        for col in data:
            if col["EXAM_LANGUAGE"] == language.upper() or col["EXAM_LANGUAGE"] == "BOTH":
                calendar[int(col["DAY"])][col["FI"]] = col["KOODI"]

    return calendar


def get_meb_names_and_codes(language: str):
    with open(file_path, "r", encoding="utf-8") as meb_csv:
        data = csv.DictReader(meb_csv, delimiter=";")

        names_and_codes = {}

        for col in data:
            if col["EXAM_LANGUAGE"] == language.upper() or col["EXAM_LANGUAGE"] == "BOTH":
                names_and_codes[col["FI"]] = col["KOODI"]
                names_and_codes[col["KOODI"]] = col["FI"]

    return names_and_codes
