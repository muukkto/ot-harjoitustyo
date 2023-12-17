import csv
import os
from pathlib import Path

MEB_EXAM_CODES_FILENAME = os.getenv(
    "MEB_EXAM_CODES_FILENAME") or "meb_exam_codes.csv"
MEB_EXAM_DAYS_FILENAME = os.getenv(
    "MEB_EXAM_DAYS_FILENAME") or "meb_exam_days.csv"

dirname = Path(__file__).parent


def get_meb_codes(language: str) -> list:
    file_path = dirname.joinpath(MEB_EXAM_CODES_FILENAME)
    with open(file_path, "r", encoding="utf-8") as meb_csv:
        data = csv.DictReader(meb_csv, delimiter=";")

        codes = []

        for col in data:
            if col["EXAM_LANGUAGE"] == language.upper() or col["EXAM_LANGUAGE"] == "BOTH":
                codes.append(col["KOODI"])

    return codes


def get_meb_names_and_codes_by_day(language: str) -> dict:
    file_path = dirname.joinpath(MEB_EXAM_CODES_FILENAME)
    with open(file_path, "r", encoding="utf-8") as meb_csv:
        data = csv.DictReader(meb_csv, delimiter=";")

        calendar = {}

        for day in range(1, 9):
            calendar[day] = {"(none)": None}

        for col in data:
            if col["EXAM_LANGUAGE"] == language.upper() or col["EXAM_LANGUAGE"] == "BOTH":
                calendar[int(col["DAY"])][col[language.upper()]] = col["KOODI"]

    return calendar


def get_meb_names_and_codes(language: str) -> dict:
    file_path = dirname.joinpath(MEB_EXAM_CODES_FILENAME)
    with open(file_path, "r", encoding="utf-8") as meb_csv:
        data = csv.DictReader(meb_csv, delimiter=";")

        names_and_codes = {}

        for col in data:
            if col["EXAM_LANGUAGE"] == language.upper() or col["EXAM_LANGUAGE"] == "BOTH":
                names_and_codes[col[language.upper()]] = col["KOODI"]
                names_and_codes[col["KOODI"]] = col[language.upper()]

    return names_and_codes


def get_meb_days(language: str) -> dict:
    file_path = dirname.joinpath(MEB_EXAM_DAYS_FILENAME)
    with open(file_path, "r", encoding="utf-8") as meb_days_csv:
        data = csv.DictReader(meb_days_csv, delimiter=";")

        days = {}

        for col in data:
            days[int(col["DAY"])] = col[language.upper()]

    return days
