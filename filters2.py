"""Provide filters for querying close approaches and limit the generated results."""
import itertools
from datetime import datetime

def create_filters(date=None, start_date=None, end_date=None,
                   distance_min=None, distance_max=None,
                   velocity_min=None, velocity_max=None,
                   diameter_min=None, diameter_max=None,
                   hazardous=None):
    """Create a collection of filters from user-specified criteria.

    Each of these arguments is provided by the main module with a value from the
    user's options at the command line. Each one corresponds to a different type
    of filter. For example, the `--date` option corresponds to the `date`
    argument, and represents a filter that selects close approaches that occured
    on exactly that given date. Similarly, the `--min-distance` option
    corresponds to the `distance_min` argument, and represents a filter that
    selects close approaches whose nominal approach distance is at least that
    far away from Earth. Each option is `None` if not specified at the command
    line (in particular, this means that the `--not-hazardous` flag results in
    `hazardous=False`, not to be confused with `hazardous=None`).

    ----------------------------------------------
    date: when a matching CloseApproach occurs (datetime)
    start_date: a time (on or after) when a matching CloseApproach occurs (datetime)
    end_date: a time (on or before) when a matching CloseApproach occurs (datetime)
    distance_min: a minimum nominal approach distance for a matching CloseApproach (float)
    distance_max: a maximum nominal approach distance for a matching CloseApproach (float)
    velocity_min: a minimum relative approach velocity for a matching CloseApproach (float)
    velocity_max: a maximum relative approach velocity for a matching CloseApproach (float)
    diameter_min: a minimum diameter of the NEO of a matching CloseApproach (float)
    diameter_max: a maximum diameter of the NEO of a matching CloseApproach (float)
    hazardous: whether the NEO of a matching CloseApproach is potentially hazardous (bool)

    RETURN:
    filters: a collection of data for use with `query` (tuple)
    """
    if date:
        date = datetime.strptime(date, "%Y-%b-%d %H:%M")
        
    if start_date:
        start_date = datetime.strptime(start_date, "%Y-%b-%d %H:%M")
        
    if end_date:
        end_date = datetime.strptime(end_date, "%Y-%b-%d %H:%M")
    
    if distance_min:
        distance_min = float(distance_min)
        
    if distance_max:
        distance_max = float(distance_max)
    
    if velocity_min:
        velocity_min = float(velocity_min)
    
    if velocity_max:
        velocity_max = float(velocity_max)
    
    if diameter_min:
        diameter_min = float(diameter_min)
    
    if diameter_max:
        diameter_max = float(diameter_max)
    
    if hazardous:
        hazardous = True
    else:
        hazardous = False
        
    filters = (date, start_date, end_date, distance_min, distance_max, velocity_min, velocity_max, diameter_min, diameter_max, hazardous)
        
    return filters


def limit(iterator, n=None):
    """Produce a limited stream of values from an iterator.
    If `n` is 0 or None, don't limit the iterator at all.

    ----------------------------------------------
    iterator: An iterator of values.
    n: The maximum number of values to produce.

    YIELD:
    The first (at most) `n` values from the iterator.
    """
    if n == 0:
        return itertools.islice(iterator, 0, None, 1)
    else:
        return itertools.islice(iterator, 0, n, 1)
