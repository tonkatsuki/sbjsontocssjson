# Global vars
steamid64ident = 76561197960265728


def steamid_to_commid(steamid):
    sid_split = steamid.split(":")
    commid = int(sid_split[2]) * 2

    if sid_split[1] == "1":
        commid += 1

    commid += steamid64ident
    return commid
