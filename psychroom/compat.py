"""Cross-compatible function for Python 2 and 3.

Largely based / taken from the compat module of pandas.

"""

# pylint disable=W0611
import itertools
import functools
import sys
import types


PY3 = (sys.version_info[0] >= 3)

try:
    import __builtin__ as builtins
except ImportError:
    import builtins

if PY3:
    # Python 3
    def isidentifier(s):
        return s.isidentifier()

    def casefold(s):
        return s.casefold()

    def isdecimal(s):
        return s.isdecimal()

    def str_to_bytes(s, encoding=None):
        return s.encode(encoding or 'ascii')

    def bytes_to_str(b, encoding=None):
        return b.decode(encoding or 'utf-8')

    # have to explicitely put builtins into the namespace
    range = range
    map = map
    zip = zip
    filter = filter
    reduce = functools.reduce
    long = int
    unichr = chr

    # list producing versions of major Python iterating functions
    def lrange(*args, **kwargs):
        return list(range(*args, **kwargs))

    def lzip(*args, **kwargs):
        return list(zip(*args, **kwargs))

    def lmap(*args, **kwargs):
        return list(map(*args, **kwargs))

    def lfilter(*args, **kwargs):
        return list(filter(*args, **kwargs))

else:
    # Python 2
    import re
    _name_re = re.compile(r'[a-zA-Z_][a-zA-Z-0-9_]*$')
    _decimal_re = re.compile(r'[+-]?((\d+(\.\d*)?)|\.\d+)([eE][+-]?[0-9]+)?')

    def isidentifier(s, dotted=False):
        return bool(_name_re.match(s))

    def casefold(s):
        return s.lower()

    def isdecimal(s):
        return bool(_decimal_re.match(s))

    def str_to_bytes(s, encoding=None):
        return s

    def bytes_to_str(b, encoding=None):
        return b

    # import iterator versions of these functions
    range = xrange
    map = itertools.imap
    zip = itertools.izip
    filter = itertools.ifilter
    reduce = reduce
    long = long
    unichr = unichr

    # Python 2-builtin ranges produce lists
    lrange = builtins.range
    lzip = builtins.zip
    lmap = builtins.map
    lfilter = builtins.filter

if PY3:
    string_types = str,
    integer_types = int,
    class_types = type,
    text_type = str
    binary_type = bytes

    def u(s):
        return s

    def u_safe(s):
        return s
else:
    string_types = basestring,
    integer_types = (int, long)
    class_types = (type, types.ClassType)
    text_type = unicode
    binary_type = str

    def u(s):
        return unicode(s, "unicode_escape")

    def u_safe(s):
        try:
            return unicode(s, "unicode_escape")
        except:
            return s

string_and_binary_types = string_types + (binary_type,)

try:
    # callable reintroduced in later versions of Python
    callable = callable
except NameError:
    def callable(obj):
        return any("__call__" in klass.__dict__ for klass in type(obj).__mro__)
