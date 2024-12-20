"""
Module quixo

Ce module contient la classe Quixo qui implémente les fonctionnalités de base
du jeu Quixo. La classe Quixo inclut des méthodes pour gérer l'état de la
partie, déplacer un cube, choisir un coup et interpréter les commandes.
"""

import argparse
import copy
from plateau import Plateau
from quixo_error import QuixoError


class Quixo:
    """
    Classe représentant le jeu Quixo.

    Attributs:
    joueurs -- Liste des joueurs.
    plateau -- Instance de la classe Plateau représentant le plateau de jeu.
    """

    def __init__(self):
        """Initialise le jeu avec deux joueurs et un plateau."""
        self.joueurs = ["Joueur 1", "Joueur 2"]
        self.plateau = Plateau()

    def état_partie(self):
        """
        Retourne une copie profonde de l'état de la partie.

        Retourne:
        Une copie profonde de l'état du plateau.
        """
        return copy.deepcopy(self.plateau)

    def __str__(self):
        """
        Représentation en chaîne de caractères de la partie.

        Retourne:
        Une chaîne de caractères représentant la légende et l'état du plateau.
        """
        légende = "Légende :\nJoueur 1 : X\nJoueur 2 : O\n"
        return légende + str(self.plateau)

    def déplacer_un_cube(self, joueur, origine, direction):
        """
        Déplace un cube sur le plateau.

        Arguments:
        joueur -- Le joueur qui déplace le cube.
        origine -- La position d'origine du cube (x, y).
        direction -- La direction dans laquelle déplacer le cube.

        Soulève:
        QuixoError si le joueur est invalide ou si la direction est invalide.
        """
        if joueur not in self.joueurs:
            raise QuixoError("Joueur invalide.")
        x, y = origine
        self.plateau.insérer_un_cube(joueur[0], x, y, direction)

    def choisir_un_coup(self):
        """
        Récupère le coup à jouer au joueur.

        Retourne:
        Un tuple contenant la position d'origine (x, y) et la direction.

        Soulève:
        QuixoError si la position d'origine ou la direction est invalide.
        """
        try:
            origine = input("Entrez la position d'origine du cube (x, y) : ")
            x, y = map(int, origine.split(','))
            direction = input("Entrez la direction : ").strip().lower()
            if direction not in {"haut", "bas", "gauche", "droite"}:
                raise QuixoError("Direction invalide.")
            return (x, y), direction
        except ValueError as exc:
            raise QuixoError("Position d'origine invalide.") from exc

    @staticmethod
    def interpréter_la_commande():
        """
        Interprète la commande pour obtenir l'IDUL du joueur.

        Retourne:
        Les arguments de la ligne de commande.
        """
        parser = argparse.ArgumentParser(
            description="Quixo"
        )
        parser.add_argument(
            'idul',
            type=str,
            help="IDUL du joueur"
        )
        return parser.parse_args()
