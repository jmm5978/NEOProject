"""Extract data on near-Earth objects and close approaches from CSV and JSON files."""
import csv
import json
from models import NearEarthObject, CloseApproach



def load_neos(neo_csv_path):
    """Read near-Earth object information from a CSV file, load it into a list, and return that list.
    
    ----------------------------------------------
    neo_csv_path: a path to a CSV file containing data about near-Earth objects (str)
    neo: a NEO object (NearEarthObject)

    RETURN:
    neos: a list of NEO objects (list)
    """
    neos = []
    with open(neo_csv_path, 'r') as infile:
        reader = csv.DictReader(infile)
        for elem in reader:
            neo = NearEarthObject(elem['pdes'], elem['name'], elem['diameter'], elem['pha'])
            neos.append(neo)
    return neos


def load_approaches(cad_json_path):
    """Read close approach data from a JSON file, load it into a list, and return that list.

    ----------------------------------------------
    cad_json_path: a path to a JSON file containing data about close approaches (str)
    approach: a CloseApproach object (CloseApproach)

    RETURN:
    approaches: a list of CloseApproach objects (list)
    """
    approaches = []
    with open(cad_json_path, 'r') as infile:
        data = json.load(infile)
        for record in data['data']:
            approach = CloseApproach(record[0], record[3], record[4], record[7])
            approaches.append(approach)
    return approaches
