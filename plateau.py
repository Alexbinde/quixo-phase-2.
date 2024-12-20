"""
Module plateau

Ce module contient la classe Plateau qui implémente les fonctionnalités de base
du plateau de jeu Quixo. La classe Plateau inclut des méthodes pour générer le
plateau, obtenir et définir des éléments, insérer des cubes et vérifier les
coordonnées.
"""

import copy
from quixo_error import QuixoError


class Plateau:
    """
    Classe représentant le plateau de jeu Quixo.

    Attributs:
    plateau -- La grille du plateau de jeu.
    """

    def __init__(self, plateau=None):
        """
        Initialise le plateau avec une grille vide ou une grille donnée.

        Arguments:
        plateau -- Une grille de jeu existante ou None pour une grille vide.
        """
        self.plateau = self.generer_le_plateau(plateau)

    def __str__(self):
        """
        Représentation en chaîne de caractères du plateau.

        Retourne:
        Une chaîne de caractères représentant le plateau.
        """
        return '\n'.join(' '.join(row) for row in self.plateau)

    def état_plateau(self):
        """
        Retourne une copie profonde de l'état du plateau.

        Retourne:
        Une copie profonde de la grille du plateau.
        """
        return copy.deepcopy(self.plateau)

    def generer_le_plateau(self, plateau):
        """
        Génère une grille de plateau valide.

        Arguments:
        plateau -- Une grille de jeu existante ou None pour une grille vide.

        Retourne:
        Une grille de plateau valide.

        Soulève:
        QuixoError si le format du plateau est invalide.
        """
        if plateau is None:
            return [[' ' for _ in range(5)] for _ in range(5)]
        if len(plateau) != 5 or any(len(row) != 5 for row in plateau):
            raise QuixoError("Format du plateau invalide.")
        for row in plateau:
            for cell in row:
                if cell not in {' ', 'X', 'O'}:
                    raise QuixoError("Format du plateau invalide.")
        return plateau

    def __getitem__(self, position):
        """
        Obtient la valeur à la position donnée sur le plateau.

        Arguments:
        position -- Un tuple (x, y) représentant la position.

        Retourne:
        La valeur à la position donnée.

        Soulève:
        QuixoError si les coordonnées sont invalides.
        """
        x, y = position
        if not (0 <= x < 5 and 0 <= y < 5):
            raise QuixoError("Coordonnées invalides.")
        return self.plateau[x][y]

    def __setitem__(self, position, value):
        """
        Définit la valeur à la position donnée sur le plateau.

        Arguments:
        position -- Un tuple (x, y) représentant la position.
        value -- La valeur à définir (' ', 'X' ou 'O').

        Soulève:
        QuixoError si les coordonnées ou la valeur sont invalides.
        """
        x, y = position
        if not (0 <= x < 5 and 0 <= y < 5):
            raise QuixoError("Coordonnées invalides.")
        if value not in {' ', 'X', 'O'}:
            raise QuixoError("Valeur invalide.")
        self.plateau[x][y] = value

    def insérer_par_le_bas(self, cube, x, y):
        """
        Insère un cube par le bas à la position donnée.

        Arguments:
        cube -- Le cube à insérer ('X' ou 'O').
        x -- La coordonnée x de la position.
        y -- La coordonnée y de la position.

        Soulève:
        QuixoError si les coordonnées sont invalides.
        """
        if not (0 <= x < 5 and 0 <= y < 5):
            raise QuixoError("Coordonnées invalides.")
        for i in range(4, 0, -1):
            self[x, i] = self[x, i - 1]
        self[x, 0] = cube

    def insérer_par_le_haut(self, cube, x, y):
        """
        Insère un cube par le haut à la position donnée.

        Arguments:
        cube -- Le cube à insérer ('X' ou 'O').
        x -- La coordonnée x de la position.
        y -- La coordonnée y de la position.

        Soulève:
        QuixoError si les coordonnées sont invalides.
        """
        if not (0 <= x < 5 and 0 <= y < 5):
            raise QuixoError("Coordonnées invalides.")
        for i in range(4):
            self[x, i] = self[x, i + 1]
        self[x, 4] = cube

    def insérer_par_la_gauche(self, cube, x, y):
        """
        Insère un cube par la gauche à la position donnée.

        Arguments:
        cube -- Le cube à insérer ('X' ou 'O').
        x -- La coordonnée x de la position.
        y -- La coordonnée y de la position.

        Soulève:
        QuixoError si les coordonnées sont invalides.
        """
        if not (0 <= x < 5 and 0 <= y < 5):
            raise QuixoError("Coordonnées invalides.")
        for i in range(4, 0, -1):
            self[i, y] = self[i - 1, y]
        self[0, y] = cube

    def insérer_par_la_droite(self, cube, x, y):
        """
        Insère un cube par la droite à la position donnée.

        Arguments:
        cube -- Le cube à insérer ('X' ou 'O').
        x -- La coordonnée x de la position.
        y -- La coordonnée y de la position.

        Soulève:
        QuixoError si les coordonnées sont invalides.
        """
        if not (0 <= x < 5 and 0 <= y < 5):
            raise QuixoError("Coordonnées invalides.")
        for i in range(4):
            self[i, y] = self[i + 1, y]
        self[4, y] = cube

    def insérer_un_cube(self, cube, x, y, direction):
        """
        Insère un cube dans la direction spécifiée à la position donnée.

        Arguments:
        cube -- Le cube à insérer ('X' ou 'O').
        x -- La coordonnée x de la position.
        y -- La coordonnée y de la position.
        direction -- La direction dans laquelle insérer le cube ('haut', 'bas',
        'gauche', 'droite').

        Soulève:
        QuixoError si la valeur ou la direction est invalide.
        """
        if cube not in {'X', 'O'}:
            raise QuixoError("Valeur invalide.")
        if direction == "bas":
            self.insérer_par_le_bas(cube, x, y)
        elif direction == "haut":
            self.insérer_par_le_haut(cube, x, y)
        elif direction == "gauche":
            self.insérer_par_la_gauche(cube, x, y)
        elif direction == "droite":
            self.insérer_par_la_droite(cube, x, y)
        else:
            raise QuixoError("Direction invalide.")
