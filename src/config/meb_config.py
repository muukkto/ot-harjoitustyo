import csv
from pathlib import Path

dirname = Path(__file__).parent
file_path = dirname.joinpath("meb_course_codes.csv")


def get_meb_codes():
    with open(file_path, "r", encoding="utf-8") as meb_csv:
        data = csv.DictReader(meb_csv, delimiter=";")

        codes = []

        for col in data:
            codes.append(col["KOODI"])

    return codes
