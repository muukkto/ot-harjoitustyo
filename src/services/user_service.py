from objects.user import User

from repositories import plan_repository


class UserService:
    """Luokka, josa vastaa käyttäjähallinnasta

    Attributes:
        user: nykyinen käyttäjän
    """

    def __init__(self):
        """Luokan konstruktori. Luo uuden käyttäjistä vastaavan palvelun.

        Nykyinen käyttäjä on aluksi None.
        """
        self._user = None

    def login(self, username: str) -> bool:
        """Kirjaa käyttäjän sisälle

        Kirjautuminen onnistuu vain, jos käyttäjä löytyy tietokannasta.

        Args:
            username (str): Käyttäjätunnus

        Returns:
            bool: Onnistuiko sisäänkirjaus
        """
        if plan_repository.find_user(username):
            self._user = User(username)
            return True

        return False

    def logout(self):
        """Kirjaa käyttäjän ulos
        """
        self._user = None

    def create_user(self, username: str) -> bool:
        """Luo uuden käyttäjän

        Käyttäjän luominen onnistuu vain, jos käyttäjätunnusta ei ole varattu

        Args:
            username (str): Käyttäjätunnus

        Returns:
            bool: Onnistuiko luominen
        """
        if plan_repository.find_user(username):
            return False

        user = plan_repository.create_user(username)
        self._user = User(user)

        return True

    def get_current_username(self) -> str:
        """Palauttaa sisäänkirjautuneen käyttäjän tunnuksen

        Returns:
            str: Nykyisen käyttäjän tunnus
        """
        if self._user:
            return self._user.get_username()

        return None
