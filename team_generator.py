import os
import random

ship_types = set({'CV', 'IXv', 'CVL', 'SS', 'BB', 'BM', 'CB', 'CL', 'IXm', 'CA', 'BC', 'SSV', 'DD', 'AE', 'AR', 'IXs', 'BBV'})
vanguard_types = set({'DD', 'CA', 'CB', 'CL', 'IXv'})

# TODO refactor into more proper file
def ingest_ships(csv_directory, level):
    vanguard_ships = list()
    main_ships = list()
    for f in os.listdir(csv_directory):
        # ensure level is one of the valid numbers
        if str(level) not in ['1', '100', '120', '125']:
            raise Exception(f"invalid value for 'level': {level} not in ['1', '100', '120', '125']")
        # we only take the files of the corresponding level
        if str(level) not in f:
            continue
        file = csv_directory + f
        if not os.path.isfile(file):
            continue
        with open(file, "rt", encoding="utf-8") as csv:
            content = csv.readlines()
        keys = content.pop(0).strip().split(',')
        for c in content:
            if len(c) < 10: # Ignore empty lines
                continue
            vals = c.strip().split(',')
            obj = {k:v for (k,v) in zip(keys, vals)}
        if obj['Type'] in vanguard_types:
            vanguard_ships.append(obj)
        else:
            main_ships.append(obj)
    return vanguard_ships, main_ships

def get_3_random_ships(list_of_ships):
    return random.sample(list_of_ships, 3)

def get_random_fleet(vanguard_ships, main_ships):
    main     = get_3_random_ships(main_ships)
    vanguard = get_3_random_ships(vanguard_ships)
    return vanguard, main


if __name__ == "__main__":
    csv_files = "./csv_files/"
    vanguard_ships, main_ships = ingest_ships(csv_files, 100)
    vanguard, main = get_random_fleet(vanguard_ships, main_ships)
    print("### VANGUARD ###")
    for s in vanguard:
        print(s['Ship Name'], s['Firepower'])
    print("### MAIN ###")
    for s in main:
        print(s['Ship Name'], s['Firepower'])