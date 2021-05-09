import json
from datetime import datetime


def write_json(data, filename="dummy.json"):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4, sort_keys=True)


def write_found(id, idInfo):
    with open("foundIds.json") as json_file:
        data = json.load(json_file)
        data["totalFound"] = data["totalFound"] + 1
        data["lastFoundId"] = id
        data["lastUpdate"] = datetime.utcnow().strftime("%d/%m/%Y, %H:%M:%S")
        temp = data["foundIdsInfo"]
        temp.append(idInfo)
        write_json(data, "foundIds.json")


def write_not_found(id):
    with open("notFoundIds.json") as json_file:
        data = json.load(json_file)
        data["totalNotFound"] = data["totalNotFound"] + 1
        data["lastNotFoundId"] = id
        data["lastUpdate"] = datetime.utcnow().strftime("%d/%m/%Y, %H:%M:%S")
        temp = data["notFoundIds"]
        temp.append(id)
        write_json(data, "notFoundIds.json")


def write_worng(id, filename="worngList.json"):
    with open(filename) as json_file:
        data = json.load(json_file)
        data["totalWorng"] = data["totalWorng"] + 1
        data["lastWorngId"] = id
        data["lastUpdate"] = datetime.utcnow().strftime("%d/%m/%Y, %H:%M:%S")
        temp = data["worngIds"]
        temp.append(id)
        write_json(data, filename)


def write_url(id, url):
    with open("urlList.json") as json_file:
        data = json.load(json_file)
        data["totalUrl"] = data["totalUrl"] + 1
        data["lastUrlId"] = id
        data["lastUpdate"] = datetime.utcnow().strftime("%d/%m/%Y, %H:%M:%S")
        temp = data["urlList"]
        temp.append(url)
        write_json(data, "urlList.json")

def write_login_and_pdf_url(id, urlData):
    with open("loginAndPdfUrl.json") as json_file:
        data = json.load(json_file)
        data["totalLoginAndPdfUrl"] = data["totalLoginAndPdfUrl"] + 1
        data["lastLoginAndPdfUrlId"] = id
        data["lastUpdate"] = datetime.utcnow().strftime("%d/%m/%Y, %H:%M:%S")
        temp = data["loginAndPdfUrl"]
        temp.append(urlData)
        write_json(data, "loginAndPdfUrl.json")

def write_login_id_and_pass(id, uData):
    with open("loginIdAndPass.json") as json_file:
        data = json.load(json_file)
        data["totalLoginIdAndPass"] = data["totalLoginIdAndPass"] + 1
        data["lastLoginIdAndPass"] = id
        data["lastUpdate"] = datetime.utcnow().strftime("%d/%m/%Y, %H:%M:%S")
        temp = data["loginIdAndPass"]
        temp.append(uData)
        write_json(data, "loginIdAndPass.json")


# with open("userIds.json") as json_file:
#     data = json.load(json_file)
#     temp = data["userIds"]
#     y = ["123458", "123459"]
#     b = y + temp
#     print(b)
#     temp.extend(y)
#     print(temp)
#     # temp.append(y)
#     print(temp)
#     write_json(data, "userIds.json")

