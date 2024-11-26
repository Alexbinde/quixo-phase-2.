# quixo_error.py
class QuixoError(Exception):
    """Exception levée pour signaler les erreurs de jeu dans Quixo."""
    def __init__(self, message):
        super().__init__(message)
