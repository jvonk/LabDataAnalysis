import os
import re
from typing import Any

import numpy.typing as npt
import scipy.constants

from .constants import hbar, m_e, c, k_B, e

conversions = {}
# Conversions based on NIST constants and natural unit definitions
conversions["second"] = conversions["s"] = (
    hbar / m_e / c**2
) / (scipy.constants.hbar / scipy.constants.m_e / scipy.constants.c**2)
conversions["metre"] = conversions["meter"] = conversions["m"] = (
    hbar / m_e / c
) / (scipy.constants.hbar / scipy.constants.m_e / scipy.constants.c)
conversions["joule"] = conversions["J"] = (m_e * c**2) / (
    scipy.constants.m_e * scipy.constants.c**2
)
conversions["kelvin"] = conversions["K"] = (
    m_e * c**2 / k_B
) / (scipy.constants.m_e * scipy.constants.c**2 / scipy.constants.k)
conversions["coulomb"] = conversions["C"] = e / scipy.constants.e
conversions["electronvolt"] = conversions["eV"] = (
    conversions["joule"] * scipy.constants.eV
)

# Derived from base units
conversions["gram"] = conversions["g"] = (
    conversions["J"] / conversions["m"] ** 2 * conversions["s"] ** 2 / 1e3
)
conversions["amphere"] = conversions["A"] = conversions["C"] / conversions["s"]
conversions["volt"] = conversions["V"] = conversions["J"] / conversions["C"]
conversions["newton"] = conversions["N"] = conversions["J"] / conversions["m"]
conversions["watt"] = conversions["W"] = conversions["J"] / conversions["s"]
conversions["tesla"] = conversions["T"] = (
    conversions["J"] / conversions["A"] / conversions["m"] ** 2
)
conversions["farad"] = conversions["F"] = conversions["C"] / conversions["V"]
conversions["hertz"] = conversions["Hz"] = 1 / conversions["s"]

conversions["ohm"] = conversions["Ω"] = conversions["V"] / conversions["A"]
conversions["henry"] = conversions["H"] = conversions["V"] * conversions["s"] / conversions["A"]

# Defined as 1
conversions["radian"] = conversions["rad"] = 1
conversions["1"] = 1

prefixes = {}
# Prefixes introduced in 2022 only exist on newer versions of scipy
prefixes["quetta"] = prefixes["Q"] = scipy.constants.quetta
prefixes["ronna"] = prefixes["R"] = scipy.constants.ronna
prefixes["yotta"] = prefixes["Y"] = scipy.constants.yotta
prefixes["zetta"] = prefixes["Z"] = scipy.constants.zetta
prefixes["exa"] = prefixes["E"] = scipy.constants.exa
prefixes["peta"] = prefixes["P"] = scipy.constants.peta
prefixes["tera"] = prefixes["T"] = scipy.constants.tera
prefixes["giga"] = prefixes["G"] = scipy.constants.giga
prefixes["mega"] = prefixes["M"] = scipy.constants.mega
prefixes["kilo"] = prefixes["k"] = scipy.constants.kilo
prefixes["hecto"] = prefixes["h"] = scipy.constants.hecto
prefixes["deka"] = prefixes["deca"] = prefixes["da"] = scipy.constants.deka
prefixes[""] = 1
prefixes["deci"] = prefixes["d"] = scipy.constants.deci
prefixes["centi"] = prefixes["c"] = scipy.constants.centi
prefixes["milli"] = prefixes["m"] = scipy.constants.milli
prefixes["micro"] = prefixes["μ"] = prefixes["u"] = scipy.constants.micro
prefixes["nano"] = prefixes["n"] = scipy.constants.nano
prefixes["pico"] = prefixes["p"] = scipy.constants.pico
prefixes["femto"] = prefixes["f"] = scipy.constants.femto
prefixes["atto"] = prefixes["a"] = scipy.constants.atto
prefixes["zepto"] = prefixes["z"] = scipy.constants.zepto
prefixes["yocto"] = prefixes["y"] = scipy.constants.yocto
prefixes["ronto"] = prefixes["r"] = scipy.constants.ronto
prefixes["quecto"] = prefixes["q"] = scipy.constants.quecto

__all__ = ["__wrapped__", "__test__"]
__path__ = [os.path.dirname(__file__)]

__test__ = dict()

@property
def __wrapped__(self):
    return self.function

def __getattr__(name: str) -> Any:
    if name in globals():
        return globals()[name]
    if name in conversions:
        return conversions[name]
    foundPrefixes = list(filter(name.startswith, prefixes))
    if len(foundPrefixes) < 1:
        raise ValueError(f"Unit {name} is not recognized")
    prefix = max(foundPrefixes, key=len)
    name = name[len(prefix) :]
    if prefix in prefixes and name in conversions:
        return prefixes[prefix] * conversions[name]
    raise ValueError(f"Unit `{prefix}{name}` is not recognized")

if __name__ == "__main__":
    import doctest

    doctest.testmod()
