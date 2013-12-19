"""Unit base class, subclasses and associated methods."""

from collections import OrderedDict

from prefix_library import prefix_library
from unit_library import unit_library
from util import DEG_SYMBOL


class IncompatibleUnitsError(Exception):

    """Exception raised for imcompatible units.

    IncompatibleUnitsError is raised when operations betweeen
    incompatible units are attempted.

    Parameters
    ----------
    message : explanation of the error

    """

    def __init__(self, message):
        self.message = message


class UnitPrefix(object):

    "Measurement unit prefix base class."""

    def __init__(self):

        self._symbol = None
        self._magnitude = None
        self._name = None

    def _lookup(self, val):
        """Look-up prefix properties for a given prefix value.

        Parameters
        ==========
        val : str or int
            prefix argument either in the form of a char, a string, or
            an integer equal to the name, symbol, or magnitude of the
            prefix

        """

        p_lib = self._library()

        if val in p_lib:
            self.name = val
            self.symbol = p_lib[val].symbol
            self.magnitude = p_lib[val].magnitude
        elif isinstance(val, int) or isinstance(val, float):
            for key, info in p_lib.items():
                if info.magnitude == val:
                    self.name = key
                    self.symbol = info.symbol
                    self.magnitude = info.magnitude
                    break
        elif isinstance(val, str) and len(val) == 1:
            for key, info in p_lib.items():
                if info.symbol == val:
                    self.name = key
                    self.symbol = info.symbol
                    self.magnitude = info.magnitude
                    break
        else:
            raise Exception('Unrecognized prefix argument.')

    def _library(self):
        """Prefix library containing prefix property mappings."""

        lib, _ = load_libraries()

        return lib

    @property
    def symbol(self):
        """Measurement unit prefix symbol, i.e. k for kilo."""
        return self._symbol

    @symbol.setter
    def symbol(self, value):
        self._symbol = value

    @property
    def magnitude(self):
        """Measurement unit prefix magnitude, i.e. 1000 for kilo."""
        return self._magnitude

    @magnitude.setter
    def magnitude(self, value):
        self._magnitude = value

    @property
    def name(self):
        """Measurement unit prefix name, i.e. kilo, micro, milli."""
        return self._name

    @name.setter
    def name(self, value):
        self._name = value


class Unit(object):

    """Measurement unit base class.

    Parameters
    ----------
    new : str, optional
        unit string name or symbol

    """

    def __init__(self, new=None):
        self._name = None
        self._symbol = None
        self._quantity = None
        self._base = None
        self._prefix = UnitPrefix()
        self._to_base = None
        self._from_base = None

        if new:
            p_str, u_str = parse_unit_string(new)
            self.prefix._lookup(p_str)
            self._lookup(u_str)

    def __format__(self, spec=None):
        if not spec:
            return str(self.symbol)
        else:
            pass

    def _lookup(self, val):
        """Look-up unit properties for a given unit value.

        Parameters
        ----------
        val : str
            a unit name or symbol string

        """

        if isinstance(val, str):
            val = val.replace('deg', DEG_SYMBOL, 1)
        else:
            raise Exception('Argument val not a string.')

        u_lib = self._library()
        if val in u_lib:
            self.quantity = u_lib[val].quantity
            self.name = u_lib[val].name
            self.symbol = u_lib[val].symbol
            self.base = u_lib[val].base
            self.to_base = u_lib[val].to_base
            self.from_base = u_lib[val].from_base
        else:
            for key, info in u_lib.items():
                if info.symbol == val:
                    self.quantity = info.quantity
                    self.name = info.name
                    self.symbol = info.symbol
                    self.base = info.base
                    self.to_base = info.to_base
                    self.from_base = info.from_base
                    break

    def _library(self):
        """Unit library containing unit property mappings."""

        _, lib = load_libraries()

        return lib

    def to(self, new):
        """Return function that convert unit to a new unit.

        Paramters
        ---------
        new : Unit or str
            new unit type or string

        Returns
        -------
        result : func
            function that converts a value in the current unit to
            a value in the new unit

        Examples
        --------
        >>> Unit('K').to(Unit('degC'))(273.15)
        0.0

        >>> Unit('pascal').to('bar')(1000.)
        0.01

        """

        return convert(self, new)

    @property
    def name(self):
        """The unit name property, i.e. degree Celsius, kilopascal."""
        return self._name

    @name.setter
    def name(self, value):
        if self._prefix.name:
            self._name = self._prefix.name + value
        else:
            self._name = value

    @property
    def symbol(self):
        """The unit symbol property, i.e. degree kPa, W, etc."""
        return self._symbol

    @symbol.setter
    def symbol(self, value):
        if self._prefix.symbol:
            self._symbol = self._prefix.symbol + value
        else:
            self._symbol = value

    @property
    def quantity(self):
        """The unit quantity property, i.e. temperature, pressure."""
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        self._quantity = value

    @property
    def base(self):
        """The base name of the unit type property, i.e. Kelvin, pascal."""
        return self._base

    @base.setter
    def base(self, value):
        self._base = value

    @property
    def prefix(self):
        """The unit prefix type property, i.e. kilo, micro."""
        return self._prefix

    @prefix.setter
    def prefix(self, value):
        self._prefix = value

    @property
    def to_base(self):
        """Function to convert a value in the unit to the base unit."""
        return self._to_base

    @to_base.setter
    def to_base(self, func):
        if self.prefix.magnitude:
            if self.quantity == 'temperature':
                self._to_base = lambda x: func(self.prefix.magnitude * x)
            else:
                self._to_base = lambda x: self.prefix.magnitude * func(x)
        else:
            self._to_base = func

    @property
    def from_base(self):
        """Function to convert a value from the base unit to the unit."""
        return self._from_base

    @from_base.setter
    def from_base(self, func):
        if self.prefix.magnitude:
            if self.quantity == 'temperature':
                self._from_base = lambda x: func(x / self.prefix.magnitude)
            else:
                self._from_base = lambda x: func(x) / self.prefix.magnitude
        else:
            self._from_base = func

    def __str__(self):
        props = OrderedDict(sorted({'Class': self.__class__,
                                    'quantity': self.quantity,
                                    'Name': self.name}.items()))
        result = ['{0}:\t{1}\n'.format(key, val) for key, val in props.items()]

        return ''.join(result)


def load_libraries():
    """Load the units and prefixes libraries.

    Returns
    -------
    unit_library : dict
    prefix_library : dict

    """

    return prefix_library(), unit_library()


def parse_unit_string(raw):
    """Parse a unit string and return the prefix and unit strings.

    Parameters
    ----------
    raw : str
        string represention of a unit of measurement in a symbolic or
        english format

    Returns
    -------
    prefix_string : str
        string representation of the unit prefix (i.e. kilo, micro, etc.)
    unit_string : str
        string representation of the actual unit of measurement (i.e.
        pascal, meter, etc.)

    """

    p_lib, u_lib = load_libraries()

    raw = raw.replace('deg', DEG_SYMBOL, 1)
    u_str = [k for k in u_lib if raw.endswith(str(k))] or \
        [i.symbol for k, i in u_lib.items() if raw.endswith(str(i.symbol))]
    if not u_str:
        raise Exception('Unrecognized unit string {}'.format(raw))

    u_str = u_str.pop()
    raw = raw[:raw.rfind(u_str)]  # chop off unit part of raw string

    if not raw:
        p_str = 'none'
    else:
        p_str = [k for k in p_lib if raw.endswith(str(k))] or \
            [i.symbol for k, i in p_lib.items() if raw.endswith(str(i.symbol))]
    if not p_str:
        raise Exception('Unrecognized prefix string {}'.format(raw))

    p_str = sorted(p_str)[-1]

    return p_str, u_str


def convert(old, new):
    """Make a function that converts from one unit to another unit.

    Parameters
    ----------
    old : Unit or str
        Unit class or str to convert from
    new : Unit or str
        Unit class or str to convert to

    Returns
    -------
    old_to_new : func
        function that whose input is a value in the old units and
        returns a value in the new units

    Examples
    --------
    >>> round(convert('degC', 'degF')(0))
    32

    >>> convert(Unit('K'), 'degC')(373.15)
    100.0

    >>> convert(Unit('Pa'), Unit('mPa'))(1.)
    1000.0

    """

    # Use duck-typing and recursion get the arguments into the expected
    # form.
    try:
        # TODO This part gets buggy, for some reason I can't get it to
        # raise the exception when I want.
        if old.quantity == new.quantity:
            to_base = old.to_base
            from_base = new.from_base
        else:
            msg = 'conversion between {0} and {1} not possible'
            raise IncompatibleUnitsError(msg.format(old.symbol, new.symbol))
    except AttributeError:
        try:
            return convert(Unit(old), Unit(new))
        except:
            try:
                return convert(old, Unit(new))
            except AttributeError:
                return convert(Unit(old), new)
            except IncompatibleUnitsError as err:
                raise err

    return lambda x: from_base(to_base(x))
