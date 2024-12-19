import random


class QuixoError(Exception):
    pass


class Quixo:
    def partie_terminée(self):
        pass


class QuixoIA(Quixo):
    def lister_les_coups_possibles(self, plateau, cube):
        if cube not in ["X", "O"]:
            raise QuixoError('Le cube doit être "X" ou "O".')
        if self.partie_terminée():
            raise QuixoError("La partie est déjà terminée.")
        coups_possibles = []
        # Logique pour lister les coups possibles
        return coups_possibles

    def analyser_le_plateau(self, plateau):
        analyse = {
            "X": {2: 0, 3: 0, 4: 0, 5: 0},
            "O": {2: 0, 3: 0, 4: 0, 5: 0}
        }
        # Logique pour analyser le plateau
        return analyse

    def partie_terminée(self):
        # Logique pour vérifier si la partie est terminée
        return None

    def trouver_un_coup_vainqueur(self, symbole):
        # Logique pour trouver un coup vainqueur
        return None

    def trouver_un_coup_bloquant(self, symbole):
        # Logique pour trouver un coup bloquant
        return None

    def jouer_un_coup(self, symbole):
        if self.partie_terminée():
            raise QuixoError("La partie est déjà terminée.")
        if symbole not in ["X", "O"]:
            raise QuixoError('Le symbole doit être "X" ou "O".')

        coup = self.trouver_un_coup_vainqueur(symbole)
        if coup is None:
            coup = self.trouver_un_coup_bloquant(symbole)
        if coup is None:
            coups_possibles = self.lister_les_coups_possibles(
                self.plateau, symbole
            )
            coup = random.choice(coups_possibles)
        # Logique pour jouer le coup
        return coup
