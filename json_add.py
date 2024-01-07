import json
import os

oldGroupsToNewGroups = {
    "serveradmin": "#css/serveradmin",
    "supporteradmin": "#css/supporteradmin",
    "officer": "#css/officer",
    "root": "#css/admin",
}

immunityGroup = {
    "serveradmin": 65,
    "supporteradmin": 75,
    "officer": 85,
    "root": 100,
}


def json_add(newfilename, user, commid, srv_group):
    group = oldGroupsToNewGroups.get(srv_group)
    immunity = immunityGroup.get(srv_group)
    newdata = {
        user: {"identity": str(commid), "immunity": immunity, "groups": [group]},
    }

    if os.path.isfile(newfilename) and os.path.getsize(newfilename) > 0:
        with open(newfilename, "r") as file:
            # Load existing data
            data = json.load(file)
    else:
        data = {}

    data.update(newdata)

    with open(newfilename, "w") as file:
        json.dump(data, file, indent=2)
