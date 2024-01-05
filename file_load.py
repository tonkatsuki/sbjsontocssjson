import json


def oldFileLoader(oldFile):
    with open(oldFile, "r") as oldAdminData:
        oldAdmins = json.load(oldAdminData)
        return oldAdmins
