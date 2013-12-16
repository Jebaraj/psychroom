"""Experimental data input/output handler functions."""
# TODO Uncertainty
from collections import namedtuple
import os
from os.path import join

import pandas as pd

from sensor_utils import translate_keys


def load_(filepath, ext='.htf', **kwargs):
    """Load a collection of test data and return pandas DataFrames.

    Parameters
    ----------
    filepath : str
        directory containing experimental data files

    Returns
    -------
    data : {pandas DataFrame}

    """

    is_ext = lambda s: True if s.endswith(ext) else False

    for root, _, files in os.walk(filepath):
        data = {
            cleanse_names([f]).pop(): read_(join(root, f), **kwargs)
            for f in filter(is_ext, sorted(files))
        }

    summary = pd.DataFrame(
        data={name: item.mean() for name, item in data.items()}
    ).T
    for id_, _ in summary.iterrows():
        for section, metadata in data[id_].metadata.items():
            for key, info in metadata.items():
                if key in summary.keys():
                    summary[key][id_], summary[key].unit = info
                else:
                    summary[key] = info.value
                    summary[key].unit = info.unit

    return data, summary


def read_(filepath_or_buffer, header=0, units=1, **kwargs):
    """Read experimental data into pandas DataFrame.

    Parameters
    ----------
    filepath_or_buffer : string or file handle / StringIO.

    header : int
        Row to use for the column labels of the parsed DataFrame.
    units : int
        Row to use for the unit properties of the parsed DataFrame.

    Returns
    -------
    result : pandas DataFrame

    """

    with open(filepath_or_buffer, 'r') as f:
        metadata = parse_metadata(f)
        result = parse_raw_data(f, **kwargs)

    result = append_metadata(result, metadata)

    return result


def parse_metadata(handle):
    """Parse test data file header metadata.

    Parameters
    ----------
    handle : test data file handle

    Returns
    -------
    metadata : dict
        parsed metadata dictionary describing test procedure

    """

    MetadataInfo = namedtuple('MetadataInfo', ['value', 'unit'])

    metadata = {}
    for line in handle:
        line = line.strip()
        if line.startswith('[raw data]'):
            return metadata
        elif line.startswith('[') and line.endswith(']'):
            section = cleanse_names([line.strip().strip('[]')]).pop()
            metadata[section] = {}
        else:
            key, info = [item.strip() for item in line.split('=')]
            key = cleanse_names([key]).pop()
            value, unit = parse_metadata_info(info)
            metadata[section][key] = MetadataInfo(*parse_metadata_info(info))


def parse_metadata_info(info):
    """Parse floating point metadata info.

    Parameters
    ----------
    info : string

    Returns
    -------
    value : float
    unit : string

    """
    value, _, unit = [item.strip() for item in info.partition('[')]
    unit = unit.strip('[]') if unit else None

    # TODO Not happy with this code, don't like logic trees in general.
    # Also, I think there is many oppurtunities for Exceptions, should
    # make this more robust.
    if unit:
        if unit.casefold() == 'bool':
            value = True if value.casefold() == 'true' else False
        elif value.isdigit():
            value = int(value)
        elif value.replace('.', '').isdecimal():
            value = float(value)

    return value, unit


def parse_raw_data(handle, **kwargs):
    """Parse raw data from test output data file.

    Parameters
    ----------
    handle : test data file handle

    Returns
    -------
    result : pandas DataFrame

    """

    read_col_metadata = lambda line: line.strip().split(',')[1:]

    column_names = cleanse_names(read_col_metadata(handle.readline()))
    column_units = read_col_metadata(handle.readline())
    result = pd.read_csv(handle, names=column_names, **kwargs)

    # TODO It would be cool if key-unit pairs were methods that updated
    # with each call.
    for key, unit in zip(result.keys(), column_units):
        result[key].unit = unit
    result.units = {key: result[key].unit for key in result.keys()}

    result = translate_keys(result, result.keys())

    return result


def cleanse_names(names, bad_chars=[], repl='_'):
    """Cleanse a list of proposed column names to correct format.

    Parameters
    ----------
    names : [string]
        A list of proposed DataFrame column name strings usually read
        from test data file raw data header or metadata information.
    bad_chars : [string]
        List of invalid or bad characters that should be replaced from
        name strings if present
    repl : string
        String replacement for bad characters in cleansed name strings.

    Returns
    -------
    result : [string]
        List of cleansed DataFrame column names.

    Examples
    >>> cleanse_names(['a b c d', 'e_f g_i', 'j_k'])
    ['a_b_c_d', 'e_f_g_i', 'j_k']

    >>> cleanse_names(['1abc0'], repl='_')
    ['_abc0']

    """

    clean = lambda x, y: x + y if (x + y).isidentifier() else x + '_'

    result = [''] * len(names)
    for ind, name in enumerate(names):
        for char in name:
            result[ind] = clean(result[ind], char)

    return result


def append_metadata(data, metadata):
    """Append metadata information to the measurement DataFrame.

    Parameters
    ----------
    data : pandas DataFrame
        measurement DataFrame associated with metadata.
    metadata : dict
        metadata dictionary usually parsed from test data file header.

    Returns
    -------
    result : pandas DataFrame
        measurement DataFrame containing additional metadata properties.

    """

    data.metadata = metadata
    for section, meta in metadata.items():
        data.__dict__[section] = pd.DataFrame(
            {key: [info.value] for key, info in meta.items()}
        )
        for key, info in meta.items():
            data.__dict__[section][key].unit = info.unit

    return data


def collapse_metadata(data, metadata):
    """Return DataFrame with metadata concatenated to columns."""

    for key, info in metadata.items():
        if key in data.keys():
            data[key][id_], data[key].unit = info
        else:
            data[key] = info.value
            data[key].unit = info.unit

    return data
