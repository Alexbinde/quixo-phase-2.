from plateau import Plateau
from quixo_error import QuixoError
import argparse


class Quixo:
    def __init__(self):
        self.joueurs = ["Joueur 1", "Joueur 2"]
        self.plateau = Plateau()

    def état_partie(self):
        """Retourne une copie profonde de l'état de la partie."""
        import copy
        return copy.deepcopy(self.plateau)

    def __str__(self):
        """Représentation en chaîne de caractères de la partie."""
        légende = "Légende :\nJoueur 1 : X\nJoueur 2 : O\n"
        return légende + str(self.plateau)

    def déplacer_un_cube(self, joueur, origine, direction):
        """Déplace un cube sur le plateau."""
        if joueur not in self.joueurs:
            raise QuixoError("Joueur invalide.")
        x, y = origine
        self.plateau.insérer_un_cube(joueur[0], x, y, direction)

    def choisir_un_coup(self):
        """Récupère le coup à jouer au joueur."""
        try:
            origine = input("Entrez la position d'origine du cube (x, y) : ")
            x, y = map(int, origine.split(','))
            direction = input("Entrez la direction : ").strip().lower()
            if direction not in {"haut", "bas", "gauche", "droite"}:
                raise QuixoError("Direction invalide.")
            return (x, y), direction
        except ValueError:
            raise QuixoError("Position d'origine invalide.")

    def interpréter_la_commande():
        parser = argparse.ArgumentParser(
            description="Quixo"
        )
        parser.add_argument(
            'idul',
            type=str,
            help="IDUL du joueur"
        )
        return parser.parse_args()
