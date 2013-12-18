"""Unit of measurements prefixes library."""
from collections import namedtuple


def prefix_library():
    """Prefix library dictionary containing unit prefix properties.

    Returns
    -------
    library : dict
        dictionary of prefix keys and property values

    """

    info = namedtuple('PrefixInfo', ['symbol', 'magnitude'])

    library = {
        'yotta': info(symbol='Y', magnitude=10 ** 24),
        'zetta': info(symbol='Z', magnitude=10 ** 21),
        'exa': info(symbol='E', magnitude=10 ** 18),
        'peta': info(symbol='P', magnitude=10 ** 15),
        'tera': info(symbol='T', magnitude=10 ** 12),
        'giga': info(symbol='G', magnitude=10 ** 9),
        'mega': info(symbol='M', magnitude=10 ** 6),
        'kilo': info(symbol='k', magnitude=10 ** 3),
        'hecto': info(symbol='h', magnitude=10 ** 2),
        'deca': info(symbol='da', magnitude=10 ** 1),
        None: info(symbol='', magnitude=1),
        'none': info(symbol='', magnitude=1),
        'deci': info(symbol='d', magnitude=10 ** -1),
        'centi': info(symbol='c', magnitude=10 ** -2),
        'milli': info(symbol='m', magnitude=10 ** -3),
        'micro': info(symbol='µ', magnitude=10 ** -6),
        'nano': info(symbol='n', magnitude=10 ** -9),
        'pico': info(symbol='p', magnitude=10 ** -12),
        'femto': info(symbol='f', magnitude=10 ** -15),
        'atto': info(symbol='a', magnitude=10 ** -18),
        'zepto': info(symbol='z', magnitude=10 ** -21),
        'yocto': info(symbol='y', magnitude=10 ** -24),
    }

    return library
