from pathlib import Path
from sqlitedict import SqliteDict

from config.config import DATABASE_FILENAME

dirname = Path(__file__).parent.joinpath("data")

if not dirname.is_dir():
    dirname.mkdir()

database_path = dirname.joinpath(DATABASE_FILENAME)

connection = SqliteDict(database_path)

def get_database_connection() -> SqliteDict:
    """Palauttaa tietokantayhteyden

    Returns:
        SqliteDict: Tietokantayhteys jota voi hallinnoida samoilla komennoilla, kuin dict-objektia.
    """

    return connection
