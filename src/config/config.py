import os
from pathlib import Path
from dotenv import load_dotenv

from services.file_service import import_curriculum_from_json
from config.meb_config import get_meb_days

dirname = Path(__file__).parent
file_path = dirname.joinpath("meb_course_codes.csv")

try:
    load_dotenv(dotenv_path=dirname.joinpath(".env"))
except FileNotFoundError:
    pass

DATABASE_FILENAME = os.getenv("DATABASE_FILENAME") or "database.sqlite"
MAX_MEB_PERIODS = int(os.getenv("MAX_MEB_PERIODS")) or 3
N_MEB_DAYS = len(get_meb_days("EN"))

CURRICULUM_FILENAME = os.getenv("CURRICULUM_FILENAME") or "lops21_curriculum.json"
CURRICULUM_PATH = dirname.joinpath(CURRICULUM_FILENAME)
CURRICULUM = import_curriculum_from_json(CURRICULUM_PATH)
