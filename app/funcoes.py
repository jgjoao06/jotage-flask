import requests


def retornaID(email):
    email = email

    r = requests.get(f'https://inchurch.pipedrive.com/api/v1/persons/search?fields=email&exact_match=true&term={email}&api_token=778d22f1ba772eb079690d5d0fd36a603f146c22')

    resposta_r = r.json()

    return(str(resposta_r['data']['items'][0]['item']['organization']['id']))



def retornaLink(email):
    id = retornaID(email)

    g = requests.get(f'https://inchurch.pipedrive.com/api/v1/organizations/{id}?api_token=778d22f1ba772eb079690d5d0fd36a603f146c22')

    resposta_g = g.json()

    return(str(resposta_g['data']['5a3a884011009c28ac9ac8b8d15849cbd84f96bf']))

