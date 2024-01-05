import json

oldGroupsToNewGroups = {
    "serveradmin": "#css/serveradmin",
    "supporteradmin": "#css/supporteradmin",
    "officer": "#css/officer",
    "root": "#css/admin",
}

immunityGroup = {
    "serveradmin": "65",
    "supporteradmin": "75",
    "officer": "85",
    "root": "100",
}


def json_make(user, commid, srv_group):
    group = oldGroupsToNewGroups.get(srv_group)
    immunity = immunityGroup.get(srv_group)
    data = {
        user: {"identity": commid, "immunity": immunity, "groups": [group]},
    }

    json_data = json.dumps(data, indent=2)
    print(json_data)
