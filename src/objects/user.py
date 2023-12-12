class User:
    """Luokka, joka vastaa käyttäjäobjekteista

    Attributes:
        username: käyttäjätunnus
    """

    def __init__(self, username: str):
        """Luokan konstruktori, joka luo uuden käyttäjän.

        Args:
            username (str): käyttäjätunnus
        """
        self._username = username

    def get_username(self) -> str:
        """Palauttaa käyttäjätunnuksen

        Returns:
            str: käyttäjätunnus
        """
        return self._username
