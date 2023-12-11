import os
from pathlib import Path
from dotenv import load_dotenv

dirname = Path(__file__).parent
file_path = dirname.joinpath("meb_course_codes.csv")

try:
    load_dotenv(dotenv_path=dirname.joinpath(".env"))
except FileNotFoundError:
    pass

DATABASE_FILENAME = os.getenv("DATABASE_FILENAME") or "database.sqlite"
MAX_MEB_PERIODS = int(os.getenv("MAX_MEB_PERIODS")) or 3
N_MEB_DAYS = int(os.getenv("N_MEB_DAYS")) or 9
