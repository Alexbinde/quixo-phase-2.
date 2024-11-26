from quixo_error import QuixoError
import copy


class Plateau:
    def __init__(self, plateau=None):
        self.plateau = self.generer_le_plateau(plateau)

    def __str__(self):
        return '\n'.join(' '.join(row) for row in self.plateau)

    def état_plateau(self):
        return copy.deepcopy(self.plateau)

    def generer_le_plateau(self, plateau):
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
        x, y = position
        if not (0 <= x < 5 and 0 <= y < 5):
            raise QuixoError("Coordonnées invalides.")
        return self.plateau[x][y]

    def __setitem__(self, position, value):
        x, y = position
        if not (0 <= x < 5 and 0 <= y < 5):
            raise QuixoError("Coordonnées invalides.")
        if value not in {' ', 'X', 'O'}:
            raise QuixoError("Valeur invalide.")
        self.plateau[x][y] = value

    def insérer_par_le_bas(self, cube, x, y):
        if not (0 <= x < 5 and 0 <= y < 5):
            raise QuixoError("Coordonnées invalides.")
        for i in range(4, 0, -1):
            self[x, i] = self[x, i - 1]
        self[x, 0] = cube

    def insérer_par_le_haut(self, cube, x, y):
        if not (0 <= x < 5 and 0 <= y < 5):
            raise QuixoError("Coordonnées invalides.")
        for i in range(4):
            self[x, i] = self[x, i + 1]
        self[x, 4] = cube

    def insérer_par_la_gauche(self, cube, x, y):
        if not (0 <= x < 5 and 0 <= y < 5):
            raise QuixoError("Coordonnées invalides.")
        for i in range(4, 0, -1):
            self[i, y] = self[i - 1, y]
        self[0, y] = cube

    def insérer_par_la_droite(self, cube, x, y):
        if not (0 <= x < 5 and 0 <= y < 5):
            raise QuixoError("Coordonnées invalides.")
        for i in range(4):
            self[i, y] = self[i + 1, y]
        self[4, y] = cube

    def insérer_un_cube(self, cube, x, y, direction):
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
