import requests


URL = 'https://pax.ulaval.ca/quixo/api/a24/'


def initialiser_partie(idul, secret):
    rep = requests.post(
        URL + 'partie/',
        auth=(idul, secret)
    )
    if rep.status_code == 200:
        data = rep.json()
        return data['id'], data['état']['joueurs'], data['état']['plateau']
    elif rep.status_code == 401:
        raise PermissionError(rep.json()['message'])
    elif rep.status_code == 406:
        raise RuntimeError(rep.json()['message'])
    else:
        raise ConnectionError()


def jouer_un_coup(id_partie, origine, direction, idul, secret):
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
    elif rep.status_code == 401:
        raise PermissionError(rep.json()['message'])
    elif rep.status_code == 406:
        raise RuntimeError(rep.json()['message'])
    else:
        raise ConnectionError()


def obtenir_etat_partie(id_partie, idul, secret):
    rep = requests.get(
        f"{URL}partie/{id_partie}/",
        auth=(idul, secret)
    )
    if rep.status_code == 200:
        data = rep.json()
        return data['id'], data['état']['joueurs'], data['état']['plateau']
    elif rep.status_code == 401:
        raise PermissionError(rep.json()['message'])
    elif rep.status_code == 406:
        raise RuntimeError(rep.json()['message'])
    else:
        raise ConnectionError()