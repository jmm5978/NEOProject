"""A database encapsulating collections of near-Earth objects and their close approaches."""
from extract import load_neos, load_approaches



class NEODatabase:
    """A database of near-Earth objects and their close approaches."""
    def __init__(self, neos, approaches):
        """Create a new `NEODatabase`.
        
        ----------------------------------------------
        neos: a collection of NEO objects (list)
        approaches: a collection of CloseApproach objects (list)
        """
        self._neos = neos
        self._approaches = approaches


        """Create a dictionary of NEOs by designation

        ----------------------------------------------
        index: neo.designation (str)
        value: NEO object (NearEarthObject)

        CREATE:
        self._neos_by_designation (dict)

        HOW TO ACCESS DATA:
        self._neos_by_designation[neo.designation].designation (designation of NEO)
        self._neos_by_designation[neo.designation].name (name of NEO)
        self._neos_by_designation[neo.designation].hazardous (if NEO is hazardous, true/false)
        self._neos_by_designation[neo.designation].diameter (diameter of NEO)
        """
        self._neos_by_designation = dict()
        for neo in neos:
            self._neos_by_designation[neo.designation] = neo
        
        """Add approaches to each NEO in the dictionary
        
        ----------------------------------------------
        approach: CloseApproach object (CloseApproach)
        neo: designation of a CloseApproach object (str)
        approaches: list of CloseApproach objects (list)

        CREATE:
        neo.approaches (list) for neo in self._neos_by_designation (dict)

        HOW TO ACCESS DATA:
        self._neos_by_designation[neo.designation].approaches (list of approaches of NEO)
        """
        for approach in self._approaches:
            neo = approach._designation
            approach.neo = neo
            self._neos_by_designation[neo].approaches.append(approach)
        

    def get_neo_by_designation(self, designation):
        """Find and return an NEO by its primary designation.
        If no match is found, return `None` instead.

        ----------------------------------------------
        designation: the primary designation of the NEO (str)
        
        RETURN:
        The NEO object with the desired primary designation, or `None`.
        """
        if str(designation).upper() in list(self._neos_by_designation.keys()):
            return self._neos_by_designation[designation]
        else:
            return None

    def get_neo_by_name(self, name):
        """Find and return an NEO by its name.
        If no match is found, return `None` instead.

        ----------------------------------------------
        name: The name of the NEO (str)
        
        RETURN:
        The NEO object with the desired name, or `None`
        """
        for neo in self._neos:
            if neo.name == str(name.title()):
                return neo
            else:
                continue
        return None


    def query(self, filters=()):
        """Query close approaches to generate those that match a collection of filters.
        If no arguments are provided, generate all known close approaches.

        ----------------------------------------------
        filters: a collection of filters (tuple)
        (date, start_date, end_date, distance_min, distance_max, velocity_min, velocity_max, diameter_min, diameter_max, hazardous)

        RETURN:
        a stream of matching CloseApproach objects (CloseApproach)
        """
        for approach in self._approaches:
            if (filters[0:3] == (None, None, None)) or (approach.time.date() == filters[0]) or (filters[1] <= approach.time.date() <= filters[2]):
                if (filters[3:5] == (None, None)) or (filters[3] <= approach.distance <= filters[4]):
                    if (filters[5:7] == (None, None)) or (filters[5] <= approach.velocity <= filters[6]):
                        if (filters[7:9] == (None, None)) or (filters[7] <= approach.neo.diameter <= filters[8]):
                            if (filters[9] == None) or (filters[9] == approach.neo.hazardous):
                                yield approach
                            else:
                                continue
                        else:
                            continue
                    else:
                        continue
                else:
                    continue
            else:
                continue
