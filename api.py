"""
Module api

Ce module contient des fonctions pour interagir avec l'API du jeu Quixo. Les
fonctions incluent l'initialisation d'une partie, le jeu d'un coup, l'obtention
de l'état d'une partie et la récupération d'une partie.
"""

import requests

URL = 'https://pax.ulaval.ca/quixo/api/a24/'


def initialiser_partie(idul, secret):
    """
    Initialise une nouvelle partie.

    Arguments:
    idul -- L'IDUL du joueur.
    secret -- Le jeton personnel du joueur.

    Retourne:
    Un tuple contenant l'ID de la partie, les joueurs et le plateau.

    Soulève:
    PermissionError si l'authentification échoue.
    RuntimeError si la requête est mal formée.
    ConnectionError pour toute autre erreur de connexion.
    """
    rep = requests.post(
        URL + 'partie/',
        auth=(idul, secret)
    )
    if rep.status_code == 200:
        data = rep.json()
        return data['id'], data['état']['joueurs'], data['état']['plateau']
    if rep.status_code == 401:
        raise PermissionError(rep.json()['message'])
    if rep.status_code == 406:
        raise RuntimeError(rep.json()['message'])
    else:
        raise ConnectionError()


def jouer_un_coup(id_partie, origine, direction, idul, secret):
    """
    Joue un coup dans une partie existante.

    Arguments:
    id_partie -- L'ID de la partie.
    origine -- La position d'origine du cube (x, y).
    direction -- La direction dans laquelle déplacer le cube.
    idul -- L'IDUL du joueur.
    secret -- Le jeton personnel du joueur.

    Retourne:
    Un tuple contenant l'ID de la partie, les joueurs et le plateau.

    Soulève:
    StopIteration si la partie est terminée et un gagnant est déterminé.
    PermissionError si l'authentification échoue.
    RuntimeError si la requête est mal formée.
    ConnectionError pour toute autre erreur de connexion.
    """
    rep = requests.put(
        f"{URL}partie/{id_partie}/",
        auth=(idul, secret),
        json={
            "origine": origine,
            "direction": direction,
        }
    )
    if rep.status_code == 200:
        data = rep.json()
        if data['gagnant']:
            raise StopIteration(data['gagnant'])
        return data['id'], data['état']['joueurs'], data['état']['plateau']
    if rep.status_code == 401:
        raise PermissionError(rep.json()['message'])
    if rep.status_code == 406:
        raise RuntimeError(rep.json()['message'])
    else:
        raise ConnectionError()


def obtenir_etat_partie(id_partie, idul, secret):
    """
    Obtient l'état actuel d'une partie.

    Arguments:
    id_partie -- L'ID de la partie.
    idul -- L'IDUL du joueur.
    secret -- Le jeton personnel du joueur.

    Retourne:
    Un tuple contenant l'ID de la partie, les joueurs et le plateau.

    Soulève:
    PermissionError si l'authentification échoue.
    RuntimeError si la requête est mal formée.
    ConnectionError pour toute autre erreur de connexion.
    """
    rep = requests.get(
        f"{URL}partie/{id_partie}/",
        auth=(idul, secret)
    )
    if rep.status_code == 200:
        data = rep.json()
        return data['id'], data['état']['joueurs'], data['état']['plateau']
    if rep.status_code == 401:
        raise PermissionError(rep.json()['message'])
    if rep.status_code == 406:
        raise RuntimeError(rep.json()['message'])
    else:
        raise ConnectionError()


def recuperer_une_partie(id_partie, idul, secret):
    """
    Récupère une partie existante.

    Arguments:
    id_partie -- L'ID de la partie.
    idul -- L'IDUL du joueur.
    secret -- Le jeton personnel du joueur.

    Retourne:
    Un tuple gontenat l'ID de la partie, les joueurs, le plateau et le gagnant

    Soulève:
    PermissionError si l'authentification échoue.
    ConnectionError pour toute autre erreur de connexion.
    """
    rep = requests.get(
        f"{URL}partie/{id_partie}/",
        auth=(idul, secret)
    )
    if rep.status_code == 200:
        data = rep.json()
        id_partie = data['id']
        joueurs = data['état']['joueurs']
        plateau = data['état']['plateau']
        gagnant = data['gagnant']
        return id_partie, joueurs, plateau, gagnant
    if rep.status_code == 401:
        raise PermissionError(rep.json()['message'])
    else:
        raise ConnectionError()
