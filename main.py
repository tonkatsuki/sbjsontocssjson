import sys
from steamid_to_commid import steamid_to_commid
from file_load import oldFileLoader
from get_vars import get_vars
from json_make import json_make
from json_add import json_add


def main():
    # Take in only argument for source admins.json file from sourcebans
    oldAdmins = oldFileLoader(sys.argv[1])
    # Make new json file, timestamped
    newfilename = json_make()
    # Loop across old file and grab values for insertion into new file
    for admin in oldAdmins:
        # Grab username for description reference, old style steamid, and current group for permissionss
        user, authid, srv_group = get_vars(admin)
        # Convert to steamdid64 for future proofing
        commid = steamid_to_commid(authid)
        json_add(newfilename, user, commid, srv_group)


if __name__ == "__main__":
    main()
