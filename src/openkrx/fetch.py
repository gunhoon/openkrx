import requests


def get(svc_nm: str, api_id: str, date: str) -> list[dict]:
    base_url = 'https://data-dbg.krx.co.kr/svc/sample/apis'
    url = f'{base_url}/{svc_nm}/{api_id}'

    headers = {
        'AUTH_KEY': '74D1B99DFBF345BBA3FB4476510A4BED4C78D13A',
    }

    payload = {
        'basDd': f'{date}',
    }

    r = requests.get(url=url, params=payload, headers=headers)
    json = r.json()

    keys = list(json)
    k = keys[0]

    if k != 'OutBlock_1':
        raise Exception(f'Invalid response: {k}')

    return json[k]
