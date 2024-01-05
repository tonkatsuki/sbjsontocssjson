import sys
from steamid_to_commid import steamid_to_commid
from file_load import oldFileLoader
from get_vars import get_vars
from json_make import json_make

# Change sourcebans json and convert to CounterStrikeSharp admins.json equivalent


# serveradmin
# officer
# supporteradmin
# root


def main():
    oldAdmins = oldFileLoader(sys.argv[1])
    for admin in oldAdmins:
        user, authid, srv_group = get_vars(admin)
        commid = steamid_to_commid(authid)
        json_make(user, commid, srv_group)


if __name__ == "__main__":
    main()
