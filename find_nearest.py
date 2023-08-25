def find_nearest(value,
                 array,
                 return_value=False):
    """Find nearest value in a numpy array

    Parameters
    ----------

    value : value to search for
    array : array to search in, should be sorted.
    return_value : bool, if to return the actual values

    Returns
    -------

    """

    import numpy as np

    closest_index = (np.abs(array - value)).argmin()

    if value > np.nanmax(array):
        import warnings
        warnings.warn(f'value > np.nanmax(array) : {value} > {np.nanmax(array)}')

    if value < np.nanmin(array):
        import warnings
        warnings.warn(f'value < np.nanmin(array) : {value} < {np.nanmax(array)}')

    if not return_value: 
        return closest_index
    else:
        return closest_index, array[closest_index]