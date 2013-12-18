"""Unit of measurements library."""
from collections import namedtuple

from utils import DEG_SYMBOL


def unit_library():
    """Unit library dictionary containing unit properties.

    Returns
    -------
    library : dict
        dictionary of unit type keys and property values

    """

    BASE_TO_BASE = lambda x: x
    props = namedtuple('UnitProperty', ['symbol', 'type', 'name',
                                        'base', 'to_base', 'from_base'])
    library = {
        'kelvin': props(
            type='temperature',
            name='Kelvin',
            symbol='K',
            base='kelvin',
            to_base=BASE_TO_BASE,
            from_base=BASE_TO_BASE
        ),
        'degrees celsius': props(
            type='temperature',
            name='degrees Celsius',
            symbol=DEG_SYMBOL + 'C',
            base='kelvin',
            to_base=lambda x: x + 273.15,
            from_base=lambda x: x - 273.15
        ),
        'degrees rankine': props(
            type='temperature',
            name='degrees Rankine',
            symbol=DEG_SYMBOL + 'R',
            base='kelvin',
            to_base=lambda x: 5. / 9. * (x - 491.67) + 273.15,
            from_base=lambda x: 1.8 * (x - 273.15) + 491.67
        ),
        'degrees fahrenheit': props(
            type='temperature',
            name='degrees Fahrenheit',
            symbol=DEG_SYMBOL + 'F',
            base='kelvin',
            to_base=lambda x: 5. / 9. * (x + 459.67),
            from_base=lambda x: 1.8 * x - 459.67
        ),
        'pascal': props(
            type='pressure',
            name='pascals',
            symbol='Pa',
            base='pascal',
            to_base=BASE_TO_BASE,
            from_base=BASE_TO_BASE
        ),
        'bar': props(
            type='pressure',
            name='bar',
            symbol='bar',
            base='pascal',
            to_base=lambda x: x * 10 ** 5,
            from_base=lambda x: x * 10 ** -5
        ),
        'standard atmosphere': props(
            type='pressure',
            name='standard atmosphere',
            symbol='atm',
            base='pascal',
            to_base=lambda x: 1.01325 * x * 10 ** 5,
            from_base=lambda x: 0.98692 * x * 10 ** -5
        ),
        'pounds per square inch': props(
            type='pressure',
            name='pounds per square inch',
            symbol='psi',
            base='pascal',
            to_base=lambda x: 6.8948 * x * 10 ** 3,
            from_base=lambda x: 1.450377 * x * 10 ** -4
        ),
    }

    return library
