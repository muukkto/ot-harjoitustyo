import time
import re

def calculate_graduation_period_options() -> list:
    current_year = 2024 #time.localtime()[0]
    current_month = 1 #time.localtime()[1]

    options = []

    for i in range(10):
        if current_month < 8:
            period = "K" if i % 2 == 0 else "S"
            year = current_year + i//2
        else:
            period = "S" if i % 2 == 0 else "K"
            year = current_year + (i+1)//2

        year_period = f"{year}{period}"

        options.append(year_period)

    return options

def print_examination_period():
    graduation_period = "2025S"
    graduation_year = int(re.split(r"([SK])", graduation_period)[0])
    graduation_semester = re.split(r"([SK])", graduation_period)[1]

    MAX_MEB_PERIODS = 3

    meb_periods = {}

    for i in range(0, MAX_MEB_PERIODS):
        if graduation_semester == "S":
            exam_semester = "S" if i % 2 == 0 else "K"
            exam_year = graduation_year - (i // 2)
        else:
            exam_semester = "K" if i % 2 == 0 else "S"
            exam_year = graduation_year - ((i+1) // 2)

        meb_periods[MAX_MEB_PERIODS-i] = f"{exam_year}{exam_semester}"

    return meb_periods

print(print_examination_period())