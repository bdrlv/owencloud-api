import requests
import json

def auth(login, password):
    # параметры авторизации
    data = json.dumps({'login': login, 'password': password})
    # запрос на авторизацию
    req = requests.post("https://api.owencloud.ru/v1/auth/open/", data=data)
    answer = json.loads(req.text)
    token = "Bearer " + answer["token"]
    return token


def device_index(bearer):
    headers = {'Authorization': bearer}
    data = json.dumps({'filter': ''})
    req = requests.post("https://api.owencloud.ru/v1/device/index/", data=data, headers=headers)
    devices = json.loads(req.text)
    return devices


def device_params(bearer, device_id):
    headers = {'Authorization': bearer}
    data = json.dumps({'filter': ''})
    req = requests.post("https://api.owencloud.ru/v1/device/" + str(device_id['id']), data=data, headers=headers)
    device_params = json.loads(req.text)
    return device_params
