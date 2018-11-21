##############################################################
# read GAMMA parameter files                                 #
# Stefan Engelhardt                                          #
##############################################################

# -*- coding: utf-8 -*-

import re


class ISPPar(object):
    """Reader for ISP parameter files of the GAMMA software package.

    This class allows to read all information from filed in GAMMA's parameter file format. Each key-value pair is parsed
    and added as attributes. For instance if the parameter file contains the pair 'sensor:    TSX-1' a attribute named
    'sensor' with the value 'TSX-1' will be available.

    The values are converted to native Python types, while unit identifiers like 'dB' or 'Hz' are removed. Please see
    the GAMMA reference manual for further information on the actual file format.
    """

    _re_kv_pair = re.compile(r'^(\w+):\s*(.+)\s*')
    _re_float_literal = re.compile(r'^[+-]?(?:(?:\d*\.\d+)|(?:\d+\.?))(?:[Ee][+-]?\d+)?')

    def __init__(self, filename):
        """Parses a ISP parameter file from disk.

        Args:
            filename: The filename or file object representing the ISP parameter file.
        """
        if isinstance(filename, basestring):
            par_file = open(filename, 'r')
        else:
            par_file = filename
        try:
            par_file.readline()  # Skip header line
            for line in par_file:
                match = ISPPar._re_kv_pair.match(line)
                if not match:
                    continue  # Skip malformed lines with no key-value pairs
                key = match.group(1)
                items = match.group(2).split()
                if len(items) == 0:
                    value = None
                elif len(items) == 1:
                    value = ISPPar._parse_literal(items[0])
                else:
                    if not ISPPar._re_float_literal.match(items[0]):
                        # Value is a string literal containing whitespace characters
                        value = match.group(2)
                    else:
                        # Evaluate each item and stop at the first non-float literal
                        value = []
                        for i in items:
                            match = ISPPar._re_float_literal.match(i)
                            if match:
                                value.append(ISPPar._parse_literal(match.group()))
                            else:
                                # If the first float literal is immediately followed by a non-float literal handle the
                                # first one as singular value, e.g. in '20.0970 dB'
                                if len(value) == 1:
                                    value = value[0]
                                break
                setattr(self, key, value)
        finally:
            par_file.close()

    @staticmethod
    def _parse_literal(x):
        """Converts a object in either a integer, floating point or string literal.

        Utilizes the built-in conversion functions int, float and str to convert a arbitrary object. The functions are
        applied in that particular order.

        Args:
            x: Any object to be converted.

        Returns:
            The converted literal.
        """
        try:
            return int(x)
        except ValueError:
            try:
                return float(x)
            except ValueError:
                return str(x)
