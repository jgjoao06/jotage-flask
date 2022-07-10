import requests


def preencheLista(resp):
    data = {"case":"leads",
                "cargo":resp["leads"][0]["last_conversion"]["content"]['Seu cargo'],
                "membros":resp["leads"][0]["last_conversion"]["content"]['Número de Membros'],
                "prioridade":resp["leads"][0]["last_conversion"]["content"]['Prioridade para Implementação'],
                "urgencia":resp["leads"][0]["last_conversion"]["content"]["Nível de Urgência"],
                "nome_igreja":resp["leads"][0]["last_conversion"]["content"]["Nome da Igreja"],
                "primeiro_nome":resp["leads"][0]["last_conversion"]["content"]["nome"],
                "telefone":resp["leads"][0]["last_conversion"]["content"]["telefone"],
                "traffic_source":resp["leads"][0]["last_conversion"]["content"]["traffic_source"],
                "identificador":resp["leads"][0]["last_conversion"]["content"]["identificador"],
                "email":resp["leads"][0]["last_conversion"]["content"]["email_lead"],
                "uf":resp["leads"][0]["last_conversion"]["content"]["UF"],
                "data":resp["leads"][0]["last_conversion"]["created_at"],
                "source":resp["leads"][0]["last_conversion"]["source"],
                "source_conversion":resp["leads"][0]["last_conversion"]["conversion_origin"]["source"],
                "medium":resp["leads"][0]["last_conversion"]["conversion_origin"]["medium"],
                "value":resp["leads"][0]["last_conversion"]["conversion_origin"]["value"],
                "campaign":resp["leads"][0]["last_conversion"]["conversion_origin"]["campaign"],
                "channel":resp["leads"][0]["last_conversion"]["conversion_origin"]["channel"]}

    g = requests.post(f'https://script.google.com/macros/s/AKfycbz-NhYuRs3DzGrshsBYo7fs1V53lI4fgacOIqPAizAv5L1cShDTGjSj-0ZEfr0hTTB1/exec', json=data)

    return("ok")