"""A database encapsulating collections of near-Earth objects and their close approaches."""
from extract import load_neos, load_approaches
from filters import DateFilter, DistanceFilter, VelocityFilter, DiameterFilter, HazardousFilter



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
            designation = approach._designation
            neo = self._neos_by_designation[designation]
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


    def query(self, filters=[]):
        """Query close approaches to generate those that match a collection of filters.
        If no arguments are provided, generate all known close approaches.

        ----------------------------------------------
        filters: a collection of filters (list)
        (date, start_date, end_date, distance_min, distance_max, velocity_min, velocity_max, diameter_min, diameter_max, hazardous)

        Yield:
        a stream of matching CloseApproach objects (CloseApproach)
        """
        for approach in self._approaches:
            if filters[0] == DateFilter(operator.eq, approach[0]):
                if filters[1] == DateFilter(operator.ge, approach[1]):
                    if filters[2] == DateFilter(operator.le, approach[2]):
                        if filters[3] == DistanceFilter(operator.ge, approach[3]):
                            if filters[4] == DistanceFilter(operator.le, approach[4]):
                                if filters[5] == VelocityFilter(operator.ge, approach[5]):
                                    if filters[6] == VelocityFilter(operator.le, approach[6]):
                                        if filters[7] == DiameterFilter(operator.ge, approach[7]):
                                            if filters[8] == DiameterFilter(operator.le, approach[8]):
                                                if filters[9] == HazardousFilter(operator.eq, approach[9]):
                                                    yield approach
