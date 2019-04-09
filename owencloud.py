"""
lib for owencloud API v1 use for free
doc: https://api.owencloud.ru
"""

import requests
import json


"""
Sign UP & Sign IN
"""
#auth\open
def auth(login, password):
    data = json.dumps({'login': login, 'password': password})
    req = requests.post("https://api.owencloud.ru/v1/auth/open/", data=data)
    answer = json.loads(req.text)
    token = "Bearer " + answer["token"]
    return token

#auth\init-sign-up
def init_signup():
    req = requests.post("https://api.owencloud.ru/v1/auth/init-sign-up")
    answer = json.loads(req.text)
    return answer

#auth\sign-up
def signup(name, surname, patronymic, email, phone, skype, password, password_confirm, individualTaxpayerNumber, individualCompanyName, verifyCode, requestId, acceptAgreement):
    data = json.dumps({"name": name,"surname": surname,"patronymic": patronymic,"email": email,"phone": phone,"skype": skype,"password": password,"password_confirm": password_confirm,"individualTaxpayerNumber": individualTaxpayerNumber,"individualCompanyName": individualCompanyName,"verifyCode": verifyCode,"requestId": requestId,"acceptAgreement": acceptAgreement})
    req = requests.post("https://api.owencloud.ru/v1/auth/sign-up", data=data)
    answer = json.loads(req.text)
    return answer

#auth\resend-signup-email
def resend_signup_email(email):
    req = requests.post("https://api.owencloud.ru/v1/auth/resend-signup-email/?email=" + email)
    answer = json.loads(req.text)
    return answer

#auth\confirm-email
def confirm_email(email, accessCode):
    data = json.dumps({"email": email, "accessCode": accessCode})
    req = requests.post("https://api.owencloud.ru/v1/auth/sign-up", data=data)
    answer = json.loads(req.text)
    return answer


"""
Password recovery
"""
#later


"""
Devices information
"""
#device/index
def device_index(bearer):
    headers = {'Authorization': bearer}
    data = json.dumps({'filter': ''})
    req = requests.post("https://api.owencloud.ru/v1/device/index/", data=data, headers=headers)
    answer = json.loads(req.text)
    return answer

#device/:id
def device_params(bearer, device_id):
    headers = {'Authorization': bearer}
    data = json.dumps({'filter': ''})
    req = requests.post("https://api.owencloud.ru/v1/device/" + str(device_id), data=data, headers=headers)
    answer = json.loads(req.text)
    return answer

#device/last-dates/:id
def device_lastdates(bearer, device_id):
    headers = {'Authorization': bearer}
    data = json.dumps({'filter': ''})
    req = requests.post("https://api.owencloud.ru/v1/device/last-dates/" + str(device_id), data=data, headers=headers)
    answer = json.loads(req.text)
    return answer


"""
Devices control
"""
#category/index


#device-management/types-info


#device-management/register


#device-management/edit/:id


#device-management/delete/:id


#device-management/update-parameter-settings/:id


"""
MODBUS control
"""
#modbus/create-parameter/:id


#modbus/edit-parameter/:id


#modbus/delete-parameter/:id


"""
category MODBUS params
"""
#modbus/create-parameter-category/


#modbus/delete-parameter-category/


#modbus/modbus/rename-parameter-category/


#modbus/move-parameter/


#modbus/move-category/


"""
Parameters DATA
"""
#parameters/last-data


#parameters/data


#parameters/forward-data


#parameters/backward-data


"""
EVENT control
"""
#/event/group-by-device/


#event/categories-list


#event/list


#event/list-by-device


#event/create


#event/edit/:id


#event/delete/:id


"""
Write DATA into Parameters
"""
#parameters/write-data


#parameters/write-cancel


#parameters/write-status


"""
Write DATA LOG
"""
#device/write-log/:id


#device/write-log-active/:id


#device/write-log-backward/:id


#device/write-log-forward/:id


"""
Device EVENT
"""
#device/events-log/:id


#device/events-log/:id


#device/events-log-backward/:id


#event-log/index


#event-log/read/:id


#company/events-log


#company/alarms-count


#/v1/company/alarms-for/:companyId


"""
Write templates
"""
#write-template/list


#write-template/:id


#write-template/execution-log/:id


#write-template/execution-log-active-all/


#write-template/execution-log-forward/:id


#write-template/execution-log-backward/:id


"""
Templates control
"""
#write-template-management/register


#write-template-management/edit/:id


#write-template-management/delete/:id


#management/execute/:id


#write-template-management/stop/:id


#write-template-management/add-parameters/:id


#write-template-management/edit-parameters-values/:id


#write-template-management/delete-parameters/:id


"""
Device & Templates info
"""
#user-object/index


"""
USER control
"""
#user/edit-password/


"""
other
"""
#later