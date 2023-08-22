# huconn-ltc4020-resistor-calculator

Add ltc4020-resistor-calculator.py

    This is a simple script to calculate the best resistor combinations for
    the LTC4020 battery charger IC. It takes a desired voltage as input and
    outputs the top 10 unique resistor combinations from the expanded E24
    and E96 series.

    Example output:
    Enter desired voltage: 25.2
    Top 10 unique resistor combinations from expanded E24 series:
    RFB1: 39.00 Ohm, RFB2: 4.30 Ohm, Voltage: 25.1744 V, Diff: -0.0256 V
    RFB1: 10.00 Ohm, RFB2: 1.10 Ohm, Voltage: 25.2273 V, Diff: 0.0273 V
    RFB1: 68.00 Ohm, RFB2: 7.50 Ohm, Voltage: 25.1667 V, Diff: -0.0333 V

    Top 10 unique resistor combinations from expanded E96 series:
    RFB1: 68.10 Ohm, RFB2: 7.50 Ohm, Voltage: 25.2000 V, Diff: 0.0000 V
    RFB1: 52.30 Ohm, RFB2: 5.76 Ohm, Voltage: 25.1997 V, Diff: -0.0003 V
    RFB1: 46.40 Ohm, RFB2: 5.11 Ohm, Voltage: 25.2006 V, Diff: 0.0006 V
    RFB1: 36.50 Ohm, RFB2: 4.02 Ohm, Voltage: 25.1990 V, Diff: -0.0010 V
