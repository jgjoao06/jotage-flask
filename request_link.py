import os
import requests


def retornaID(email):
    api_token = os.environ.get('pipedrive-api_token')
    try:
        r = requests.get(f'https://inchurch.pipedrive.com/api/v1/persons/search?fields=email&exact_match=true&term={email}&api_token={api_token}')
        resposta_r = r.json()
        return(str(resposta_r['data']['items'][0]['item']['organization']['id']))
    except IndexError:
        return("Não foi possível identificar o ID no Pipedrive para este email")



def retornaLink(email):
    api_token = os.environ.get('pipedrive-api_token')
    id = retornaID(email, api_token)
    try:
        g = requests.get(f'https://inchurch.pipedrive.com/api/v1/organizations/{id}?api_token={api_token}')
        resposta_g = g.json()
        return(str(resposta_g['data']['5a3a884011009c28ac9ac8b8d15849cbd84f96bf']))
    except KeyError:
        return ("Não foi possível identificar o ID no Pipedrive para este email")