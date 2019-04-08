"""
lib for owencloud API v1
use for free
"""

import requests
import json


"""
Sign UP & Sign IN
"""
#authentication
def auth(login, password):
    data = json.dumps({'login': login, 'password': password})
    req = requests.post("https://api.owencloud.ru/v1/auth/open/", data=data)
    answer = json.loads(req.text)
    token = "Bearer " + answer["token"]
    return token


"""
Devices information
"""
#device list
def device_index(bearer):
    headers = {'Authorization': bearer}
    data = json.dumps({'filter': ''})
    req = requests.post("https://api.owencloud.ru/v1/device/index/", data=data, headers=headers)
    devices = json.loads(req.text)
    return devices

#device information
def device_params(bearer, device_id):
    headers = {'Authorization': bearer}
    data = json.dumps({'filter': ''})
    req = requests.post("https://api.owencloud.ru/v1/device/" + str(device_id['id']), data=data, headers=headers)
    device_params = json.loads(req.text)
    return device_params
