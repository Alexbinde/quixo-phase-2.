import random


class QuixoError(Exception):
    """Exception personnalisée pour les erreurs du jeu Quixo."""
    pass


class Quixo:
    """Classe de base pour le jeu Quixo."""

    def partie_terminée(self):
        """Vérifie si la partie est terminée."""
        pass

    def état_plateau(self):
        """Retourne l'état actuel du plateau."""
        pass


class Plateau:
    """Classe représentant le plateau de jeu."""

    def __init__(self, état):
        """Initialise le plateau avec l'état donné."""
        pass


class QuixoIA(Quixo):
    """Classe pour l'IA du jeu Quixo, héritant de la classe Quixo."""

    def lister_les_coups_possibles(self, plateau, cube):
        """
        Liste les coups possibles pour le joueur spécifié.

        Arguments:
        plateau -- Instance de la classe Plateau.
        cube -- Symbole du joueur ('X' ou 'O').

        Retourne:
        Une liste de dictionnaires contenant les coups possibles.
        """
        if cube not in ["X", "O"]:
            raise QuixoError('Le cube doit être "X" ou "O".')
        if self.partie_terminée():
            raise QuixoError("La partie est déjà terminée.")
        coups_possibles = []
        # Logique pour lister les coups possibles
        return coups_possibles

    def analyser_le_plateau(self, plateau):
        """
        Analyse le plateau et compte les lignes de 2, 3, 4 et 5 cubes.

        Arguments:
        plateau -- Instance de la classe Plateau.

        Retourne:
        Un dictionnaire contenant le nombre de lignes pour chaque joueur.
        """
        analyse = {
            "X": {2: 0, 3: 0, 4: 0, 5: 0},
            "O": {2: 0, 3: 0, 4: 0, 5: 0}
        }
        # Logique pour analyser le plateau
        return analyse

    def partie_terminée(self):
        """
        Vérifie si la partie est terminée.

        Retourne:
        Le nom du joueur vainqueur ou None si la partie n'est pas terminée.
        """
        # Logique pour vérifier si la partie est terminée
        return None

    def trouver_un_coup_vainqueur(self, symbole):
        """
        Trouve un coup gagnant pour le joueur spécifié.

        Arguments:
        symbole -- Symbole du joueur ('X' ou 'O').

        Retourne:
        Un coup gagnant ou None si aucun coup gagnant n'est possible.
        """
        # Logique pour trouver un coup vainqueur
        return None

    def trouver_un_coup_bloquant(self, symbole):
        """
        Trouve un coup bloquant pour le joueur spécifié.

        Arguments:
        symbole -- Symbole du joueur ('X' ou 'O').

        Retourne:
        Un coup bloquant ou None si aucun coup bloquant n'est possible.
        """
        # Logique pour trouver un coup bloquant
        return None

    def jouer_un_coup(self, symbole):
        """
        Joue un coup pour le joueur spécifié.

        Arguments:
        symbole -- Symbole du joueur ('X' ou 'O').

        Retourne:
        Le coup joué.

        Soulève:
        QuixoError si la partie est terminée ou si le symbole est invalide.
        """
        if self.partie_terminée():
            raise QuixoError("La partie est déjà terminée.")
        if symbole not in ["X", "O"]:
            raise QuixoError('Le symbole doit être "X" ou "O".')

        coup = self.stratégie_base(self.plateau, symbole)
        if coup is None:
            coup = self.stratégie_simple(self.plateau, symbole)
        if coup is None:
            coup = self.stratégie_aléatoire(self.plateau, symbole)

        # Logique pour jouer le coup
        return coup

    def simuler_coup(self, plateau, coup):
        """
        Simule un coup sur une copie du plateau.

        Arguments:
        plateau -- Instance de la classe Plateau.
        coup -- Coup à simuler.

        Retourne:
        Une nouvelle instance de Plateau après simulation du coup.
        """
        état = plateau.état_plateau()
        nouveau_plateau = Plateau(état)
        # Logique pour simuler le coup sur nouveau_plateau
        return nouveau_plateau

    def stratégie_base(self, plateau, symbole):
        """
        Stratégie de base pour trouver un coup gagnant ou bloquant.

        Arguments:
        plateau -- Instance de la classe Plateau.
        symbole -- Symbole du joueur ('X' ou 'O').

        Retourne:
        Un coup gagnant ou bloquant, ou None si aucun n'est trouvé.
        """
        coup = self.trouver_un_coup_vainqueur(symbole)
        if coup is None:
            coup = self.trouver_un_coup_bloquant(symbole)
        return coup

    def stratégie_simple(self, plateau, symbole):
        """
        Stratégie simple pour maximiser le nombre de cubes sur une ligne.

        Arguments:
        plateau -- Instance de la classe Plateau.
        symbole -- Symbole du joueur ('X' ou 'O').

        Retourne:
        Un coup pour maximiser les cubes sur une ligne, ou None.
        """
        # Logique pour maximiser le nombre de cubes sur une ligne
        return None

    def stratégie_aléatoire(self, plateau, symbole):
        """
        Stratégie aléatoire pour choisir un coup parmi les coups possibles.

        Arguments:
        plateau -- Instance de la classe Plateau.
        symbole -- Symbole du joueur ('X' ou 'O').

        Retourne:
        Un coup aléatoire parmi les coups possibles.
        """
        coups_possibles = self.lister_les_coups_possibles(plateau, symbole)
        return random.choice(coups_possibles)

    def stratégie_avancée(self, plateau, symbole):
        """
        Stratégie avancée pour simuler plusieurs coups à l'avance.

        Arguments:
        plateau -- Instance de la classe Plateau.
        symbole -- Symbole du joueur ('X' ou 'O').

        Retourne:
        Le meilleur coup possible après simulation.
        """
        # Logique pour simuler plusieurs coups à l'avance
        return None
