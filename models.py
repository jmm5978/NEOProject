"""Represent models for near-Earth objects and their close approaches."""
from helpers import cd_to_datetime, datetime_to_str



class NearEarthObject:
    """A near-Earth object (NEO)."""
    def __init__(self, pdes, name=None, diameter=float('nan'), hazardous=False):
        """Create a NearEarthObject.
        
        data imports from neos.csv
        ----------------------------------------------
        pdes: primary designation (str)
        name: name of object (str)
        diameter: diameter of object in km (float)
        hazardous: whether the object is hazardous or not (bool)
        """
        self.designation = str(pdes)
        if name == '':
            self.name = None 
        else:
            self.name = str(name)
        if hazardous.upper() == 'Y':
            self.hazardous = True
        else:
            self.hazardous = False
        try:
            self.diameter = float(diameter)
        except:
            self.diameter = float('nan')
        
        self.approaches = []
        

    @property
    def fullname(self):
        """Return a representation of the full name of this NEO."""
        return f'{self.designation} ({self.name})'


    def __str__(self):
        """Return `str(self)`."""
        if self.hazardous:
            return f"NEO {self.fullname} has a diameter of {self.diameter:.2f} km and is hazardous."
        else:
            return f"NEO {self.fullname} has a diameter of {self.diameter:.2f} km and is not hazardous."


    def __repr__(self):
        """Return `repr(self)`, a computer-readable string representation of this object."""
        return (f"NearEarthObject(designation={self.designation!r}, name={self.name!r}, "
                f"diameter={self.diameter:.3f}, hazardous={self.hazardous!r})")



class CloseApproach:
    """A close approach to Earth by an NEO."""
    def __init__(self, des, cd, dist, v_rel):
        """Create a CloseApproach object.

        data imports from cad.json
        ----------------------------------------------
        des: primary designation (str)
        cd: time of close-approach (datetime)
        dist: approach distance in au (float)
        v_rel: velocity in km/s (float)
        """
        self._designation = des
        self.time = cd_to_datetime(cd)
        try:
            self.distance = float(dist)
        except:
            self.distance = float('nan')
        try:
            self.velocity = float(v_rel)
        except:
            self.velocity = float('nan')

        self.neo = None


    @property
    def time_str(self):
        """Return a formatted representation of this `CloseApproach`'s approach time.

        The value in `self.time` should be a Python `datetime` object. While a
        `datetime` object has a string representation, the default representation
        includes seconds - significant figures that don't exist in our input
        data set.

        The `datetime_to_str` method converts a `datetime` object to a
        formatted string that can be used in human-readable representations and
        in serialization to CSV and JSON files.
        """
        return datetime_to_str(self.time)


    def __str__(self):
        """Return `str(self)`."""
        if self.neo:
            return f"On {self.time_str}, {self.neo} approaches earth at a distance of {self.distance:.2f} au and a velocity of {self.velocity:.2f} km/s."
        else:
            return f"On {self.time_str}, {self._designation} approaches earth at a distance of {self.distance:.2f} au and a velocity of {self.velocity:.2f} km/s."


    def __repr__(self):
        """Return `repr(self)`, a computer-readable string representation of this object."""
        return (f"CloseApproach(time={self.time_str!r}, distance={self.distance:.2f}, "
                f"velocity={self.velocity:.2f}, neo={self.neo!r})")
                