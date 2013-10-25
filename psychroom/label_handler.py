"""Measurement label parser."""


def translate_label(label, sep='_', component_library=None, fluid_library=None,
                    location_library=None, type_library=None):
    """Translate a label and return a descriptive string.

    Parse a standard format measurement label and produce a descriptive
    measurement name string.  The standard label is composed of the
    following parts::

        {COMPONENT}{#?}_{FLUID}{#?}_{LOCATION}{#?}_{TYPE}

    For more information of label formatting, see measurment standard
    documentation at::
        <https://github.com/ahjortland/psychroom/tree/master/docs>

    Parameters
    ----------
    label : string
        Measurement label string formatted using the Herrick
        Psychrometric Chamber Experimental Data Standard
    sep : string, optional, default '_'
        Separator character used in measurement label, optional
        parameter should only be used in special cases when default
        value, '_', cannot be used.
    component_library : dict, optional
        Component identifier dictionary used to identify the component
        the measurement was taken on. Usage not recommended since it
        deviates from experimental data standard.
    fluid_library : dict, optional
        Fluid identifier dictionary used to identify the fluid the
        measurement was observing. Usage not recommended since it
        deviates from experimental data standard.
    location_library : dict, optional
        Location identifier dictionary used to identify the location on
        the component where the measurement was taken. Usage not
        recommended since it deviates from experimental data standard.
    type_library : dict, optional
        Measurement type identifier dictionary used to identify the type
        of measurement recorded by the measurement device. Usage not
        recommended since it deviates from experimental data standard.

    Returns
    -------
    description : string if parsing succeeded
        formatted descriptive string of measurement label, useful if not
        familiar with the labelling convention

    Examples
    --------
    >>> parse_label('ahu_air_ret_T')
        'AHU return air temperature'
    >>> parse_label('cmp2_ref_in_P')
        'Compressor 2 refrigerant inlet pressure'
    >>> parse_label('idx_ref_gas4_T')
        'Indoor Heat Exchanger refrigerant gas line 4 temperature'

    """

    label = label.split(sep)
    libraries = (component_library or make_component_library(),
                 fluid_library or make_fluid_library(),
                 location_library or make_location_library(),
                 type_library or make_type_library())

    description = \
        ' '.join([translate_identifier(item, lib)
                 for item, lib in zip(label, libraries)])

    return description


def translate_identifier(token, library):
    """Translate a given label token.

    Parameters
    ----------
    token : string
        label identifier string
    library : dict
        label identifier dictionary

    Returns
    -------
    translation : string
        descriptive label translation string

    """

    try:
        return library[token]
    except:
        raise Exception("Unrecognized label identifier '{}'!".format(token))


def make_type_library():
    """Build the default measurement type library.

    Returns
    -------
    library : dict
        measurement types library

    """
    library = {
        'Cp': 'specific heat at constant pressure',
        'Cv': 'specific heat at constant volume',
        'B': 'wet bulb temperature',
        'D': 'dew point temperature',
        'dP': 'differential pressure',
        'freq': 'frequency',
        'G': 'volumetric flow rate',
        'H': 'specific entalpy',
        'I': 'current',
        'M': 'mass',
        'm': 'mass flow rate',
        'pa': 'absolute pressure',
        'pg': 'gage pressure',
        'pos': 'position',
        'pwr': 'electrical power',
        'q': 'heat transfer',
        'Q': 'quality',
        'rho': 'density',
        'RH': 'relative humidity',
        'S': 'specific entropy',
        'spd': 'speed',
        'T': 'temperature',
        'u': 'velocity',
        'V': 'voltage',
        'v': 'specific volume',
        'W': 'humidity ratio',
        'x': 'mass fraction',
    }

    return library


def make_fluid_library():
    """Build the default fluid library.

    Returns
    -------
    library : dict
        fluid library

    """
    library = {
        'air': 'air',
        'elec': 'electric',
        'gas': 'gas',
        'gly': 'glycol',
        'h20': 'water',
        'oil': 'oil',
        'ref': 'refrigerant',
    }

    return library


def make_component_library():
    """Build the default component library.

    Returns
    -------
    library : dict
        component library

    """

    library = {
        'absr': 'absorber',
        'accm': 'accumulator',
        'ahu': 'air handling unit',
        'comp': 'compressor',
        'damp': 'damper',
        'desr': 'desorber',
        'idf': 'indoor fan',
        'ehr': 'electric heater',
        'ejr': 'ejector',
        'fan': 'fan',
        'filt': 'filter',
        'idhx': 'indoor heat exchanger',
        'ithx': 'internal heat exchanger',
        'mflr': 'muffler',
        'noz': 'nozzle',
        'odhx': 'outdoor heat exchanger',
        'pump': 'pump',
        'rect': 'rectifier',
        'recv': 'receiver',
        'sep': 'separator',
        'valv': 'valve',
        'xd': 'expansion device',
    }

    return library


def make_location_library():
    """Build the default location library.

    Returns
    -------
    library : dict
        location library

    """

    library = {
        'crct': 'circuit',
        'ctrl': 'controller',
        'dis': 'discharge',
        'gasl': 'gas line',
        'in': 'inlet',
        'liql': 'liquid line',
        'mix': 'mixed',
        'odr': 'outdoor',
        'out': 'outlet',
        'ret': 'return',
        'sup': 'supply',
    }

    return library
