from pathlib import Path
from sqlitedict import SqliteDict

dirname = Path(__file__).parent.joinpath("data")

if not dirname.is_dir():
    dirname.mkdir()

database_path = dirname.joinpath("database.sqlite")

connection = SqliteDict(database_path)

def get_database_connection():
    return connection
