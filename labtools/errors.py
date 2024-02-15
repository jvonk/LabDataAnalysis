# Error Calculations for Physics 111A Lab
# Written by Ayushmaan Aggarwal
# Date Created: 1/20/2024

# Currently implemented features:
# Calculating errors from ADS and DMM

import numpy as np
from uncertainties import ufloat
from .units import V, mV, A, mA, ohm, Mohm, nF, uF


# DMM Errors
def dmm_dc_voltage(voltage, digits=0.01, bypass=False):
    """
    Calculates the error in the DC voltage and returns a ufloat
    """
    if not bypass:
        assert abs(voltage) >= 200*mV, "Voltage should be >= 200mV"
        assert abs(voltage) <= 1000*V, "Voltage should be <= 1000V"

    return ufloat(voltage, (0.5 / 100.0) * abs(voltage) + digits)


def dmm_ac_voltage(voltage, digits=0.01, bypass=False):
    """
    Calculates the error in the AC voltage and returns a ufloat
    """
    if not bypass:
        assert abs(voltage) >= 200*mV, "Voltage should be >= 200mV"
        assert abs(voltage) <= 750*V, "Voltage should be <= 750V"

    return ufloat(voltage, (0.8 / 100.0) * abs(voltage) + 3 * digits)


def dmm_dc_current(current, digits=0.01, bypass=False):
    """
    Calculates the error in the DC current and returns a ufloat
    """
    if not bypass:
        assert abs(current) >= 20*mA, "Current should be >= 20mA"
        assert abs(current) <= 20*A, "Current should be <= 20A"

    return ufloat(current, (0.8 / 100.0) * abs(current) + digits)


def dmm_ac_current(current, digits=0.01, bypass=False):
    """
    Calculates the error in the AC current and returns a ufloat
    """
    if not bypass:
        assert abs(current) >= 20*mA, "Current should be >= 20mA"
        assert abs(current) <= 20*A, "Current should be <= 20A"

    return ufloat(current, (1.0 / 100.0) * abs(current) + 3 * digits)


def dmm_resistance(resistance, digits=0.01, bypass=False):
    """
    Calculates the error in the resistance and returns a ufloat
    """
    if not bypass:
        assert abs(resistance) >= 200*ohm, "Resistance should be >= 200 ohm"
        assert abs(resistance) <= 2000*Mohm, "Resistance should be <= 2000 Mohm"

    return ufloat(resistance, (2.5 / 100.0) * abs(resistance) + 3 * digits)


def dmm_capacitance(capacitance, digits=0.01, bypass=False):
    """
    Calculates the error in the capacitance and returns a ufloat
    """
    if not bypass:
        assert abs(capacitance) >= 2*nF, "Capacitance should be >= 2nF"
        assert abs(capacitance) <= 200*uF, "Capacitance should be <= 200uF"

    return ufloat(capacitance, (2.5 / 100.0) * abs(capacitance) + 5 * digits)


def resistance(resistance):
    return ufloat(resistance, 0.01 * abs(resistance))


# ADS Errors
def ads_volt_voltmeter(voltage, digits=0.001):
    return ufloat(voltage, digits)


def ads_volt_oscilliscope(voltage, scale=0.5):
    if scale >= 1:
        return ufloat(voltage, 0.1 + (0.5 / 100.0) * abs(voltage))
    elif scale <= 0.5:
        return ufloat(voltage, 0.01 + (0.5 / 100.0) * abs(voltage))


def ads_voltage_output(voltage):
    ### WHAT IS V/div
    if voltage <= 1:
        return ufloat(voltage, 0.01 + (0.5 / 100.0) * abs(voltage))
    else:
        return ufloat(voltage, 0.025 + (0.5 / 100.0) * abs(voltage))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
