"""Unit of measurements library."""
from collections import namedtuple

from util import DEG_SYMBOL


def unit_library():
    """Unit library dictionary containing unit properties.

    Returns
    -------
    library : dict
        dictionary of unit type keys and property values

    """

    BASE_TO_BASE = lambda x: x
    props = namedtuple('UnitProperty', ['symbol', 'quantity', 'name',
                                        'base', 'to_base', 'from_base'])
    library = {
        'kelvin': props(
            quantity='temperature',
            name='Kelvin',
            symbol='K',
            base='kelvin',
            to_base=BASE_TO_BASE,
            from_base=BASE_TO_BASE
        ),
        'degrees celsius': props(
            quantity='temperature',
            name='degrees Celsius',
            symbol=DEG_SYMBOL + 'C',
            base='kelvin',
            to_base=lambda x: x + 273.15,
            from_base=lambda x: x - 273.15
        ),
        'degrees rankine': props(
            quantity='temperature',
            name='degrees Rankine',
            symbol=DEG_SYMBOL + 'R',
            base='kelvin',
            to_base=lambda x: (x - 491.67) / 1.8 + 273.15,
            from_base=lambda x: 1.8 * (x - 273.15) + 491.67
        ),
        'degrees fahrenheit': props(
            quantity='temperature',
            name='degrees Fahrenheit',
            symbol=DEG_SYMBOL + 'F',
            base='kelvin',
            to_base=lambda x: (x + 459.67) / 1.8,
            from_base=lambda x: 1.8 * x - 459.67
        ),
        'pascal': props(
            quantity='pressure',
            name='pascals',
            symbol='Pa',
            base='pascal',
            to_base=BASE_TO_BASE,
            from_base=BASE_TO_BASE
        ),
        'bar': props(
            quantity='pressure',
            name='bar',
            symbol='bar',
            base='pascal',
            to_base=lambda x: x * 10 ** 5,
            from_base=lambda x: x * 10 ** -5
        ),
        'standard atmosphere': props(
            quantity='pressure',
            name='standard atmosphere',
            symbol='atm',
            base='pascal',
            to_base=lambda x: 1.01325 * x * 10 ** 5,
            from_base=lambda x: 0.98692 * x * 10 ** -5
        ),
        'pounds per square inch': props(
            quantity='pressure',
            name='pounds per square inch',
            symbol='psi',
            base='pascal',
            to_base=lambda x: 6.8948 * x * 10 ** 3,
            from_base=lambda x: 1.450377 * x * 10 ** -4
        ),
    }

    return library
