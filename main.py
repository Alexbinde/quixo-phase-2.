from quixo import interpréter_la_commande
from api import initialiser_partie, jouer_un_coup
from quixo_error import QuixoError


def main():
    # Interpréter la commande pour obtenir l'IDUL du joueur
    args = interpréter_la_commande()
    idul = args.idul
    secret = "votre_jeton_personnel"  # Remplacez par votre jeton personnel

    try:
        # Initialiser une nouvelle partie
        id_partie, joueurs, plateau = initialiser_partie(idul, secret)
        print(f"Nouvelle partie commencée avec l'IDUL : {idul}")
        print(f"Joueurs : {joueurs}")
        afficher_plateau(plateau)

        while True:
            # Demander à l'utilisateur de spécifier son coup
            origine, direction = demander_coup()
            try:
                # Jouer un coup
                id_partie, joueurs, plateau = jouer_un_coup(
                                            id_partie, origine,
                                            direction, idul, secret
                )
                afficher_plateau(plateau)
            except QuixoError as e:
                print(f"Erreur : {e}")
            except StopIteration as gagnant:
                print(f"Partie terminée. Le gagnant est : {gagnant}")
                break

    except (PermissionError, RuntimeError, ConnectionError) as e:
        print(f"Erreur : {e}")


def afficher_plateau(plateau):
    """Affiche le plateau de jeu en art ASCII."""
    for row in plateau:
        print(' '.join(row))
    print()


def demander_coup():
    """Demande à l'utilisateur de spécifier son coup."""
    try:
        origine = input("Entrez la position d'origine du cube (x, y) : ")
        x, y = map(int, origine.split(','))
        direction = input("Entrez la direction : ").strip().lower()
        if direction not in {"haut", "bas", "gauche", "droite"}:
            raise QuixoError("Direction invalide.")
        return (x, y), direction
    except ValueError:
        raise QuixoError("Position d'origine invalide.")


if __name__ == "__main__":
    main()
