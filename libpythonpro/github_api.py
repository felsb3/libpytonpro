import requests


def buscar_avatar(usuario):
    """
    Busca o avatar de um usuário do Github

    :param usuario: str com o nome de usuário no github
    :return: str
    """
    url = f'https://api.github.com/users/{usuario}'
    resp = requests.get(url)
    return resp.json()['avatar_url']
