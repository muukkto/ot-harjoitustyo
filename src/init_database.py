from database_connection import get_database_connection


def initialize_database():
    """Alustaa tietokannan
    """
    connection = get_database_connection()
    connection.clear()


if __name__ == "__main__":
    initialize_database()
