import requests


def authUser(login: str, password: str):
    params = {
        "login": login,
        "password": password
    }
    response = requests.get("http://192.168.1.92:12222/api/user/auth", params=params)
    return response


