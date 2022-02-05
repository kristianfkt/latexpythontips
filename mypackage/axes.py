def si_prefix(prefix=None):
    """
    Return the SI-prefix for a unit
    """

    if prefix is None:
        prefix='none'
    prefix=prefix.lower()
    prefixes = {
        'micro':'$\mu$',
        'milli':'m',
        'none':'',
        'kilo':'k',
        'mega':'M'
    }
    return prefixes[prefix]


def time(unit=None):
    """
    Returns axis label for time with different units
    """
    if unit is None:
        unit='hour'
    unit=unit.lower()
    units={
        'second':'s',
        'seconds':'s',
        's':'s',
        #
        'hour':'h',
        'hours':'h',
        'h':'h'
    }
    return f'Time/{units[unit]}'

def current(prefix=None, density=None):
    """
    Return axis label for current with different prefixes and density-normalizations
    Acm^-2
    Ag^-1
    etc
    """
    if density is None:
        density='none'
    density=density.lower()
    densities = {
        'cm':'cm$^{-2}$',
        'g:':'g$^{-1}$',
        'none':''
    }
    return f'Current/{si_prefix(prefix=prefix)}A{densities[density]}'

def voltage(prefix=None, ref=None):
    """
    Return axis label for voltage. Absolute value or relative to some reference
    """
    if ref is None:
        ref='none'
    ref = ref.lower()

    refs = {
        'none':'',
        'rhe':' vs RHE',
        'nhe':' vs NHE',
        'agcl':' vs AgCl'
    }
    return f'Voltage/{si_prefix(prefix=prefix)}V{refs[ref]}'


if __name__ == '__main__':
    pass