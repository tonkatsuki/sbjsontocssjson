import json
import os
from datetime import datetime


def json_make():
    # Create a filename based on the current date and time
    newfilename = datetime.now().strftime("%Y-%m-%d_%H-%M-%S.json")

    # Check if file already exists
    if not os.path.isfile(newfilename):
        # Create a new JSON file with an empty dictionary
        with open(newfilename, "w") as file:
            json.dump({}, file)
        print(f"Created new file: {newfilename}")
        return newfilename
    else:
        print(f"File {newfilename} already exists.")
