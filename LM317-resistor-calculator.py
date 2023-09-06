''' This script calculates the best resistor combinations for the LM317 voltage regulator
    The script calculates the best resistor combinations for the given output voltage
    LM317 datasheet: https://www.ti.com/lit/ds/symlink/lm317.pdf

    LM317 voltage regulator has two resistors, R1 and R2, that set the output voltage
    The output voltage is calculated by the following formula:
    Vout = 1.25 * (1 + (R2 / R1))

    The script calculates the best resistor combinations for the given output voltage
    if 3.3V is desired, the script calculates the best resistor combinations for 3.3V

    The script considers the E24 and E96 resistor series
    The script prints the top 10 unique resistor combinations with the lowest error
'''


# E24 and E96 resistor series values
E24 = [
    1.0, 1.1, 1.2, 1.3, 1.5, 1.6, 1.8, 2.0, 2.2, 2.4,
    2.7, 3.0, 3.3, 3.6, 3.9, 4.3, 4.7, 5.1, 5.6, 6.2,
    6.8, 7.5, 8.2, 9.1
]

E96 = [
    1.00, 1.02, 1.05, 1.07, 1.10, 1.13, 1.15, 1.18, 1.21, 1.24,
    1.27, 1.30, 1.33, 1.37, 1.40, 1.43, 1.47, 1.50, 1.54, 1.58,
    1.62, 1.65, 1.69, 1.74, 1.78, 1.82, 1.87, 1.91, 1.96, 2.00,
    2.05, 2.10, 2.15, 2.21, 2.26, 2.32, 2.37, 2.43, 2.49, 2.55,
    2.61, 2.67, 2.74, 2.80, 2.87, 2.94, 3.01, 3.09, 3.16, 3.24,
    3.32, 3.40, 3.48, 3.57, 3.65, 3.74, 3.83, 3.92, 4.02, 4.12,
    4.22, 4.32, 4.42, 4.53, 4.64, 4.75, 4.87, 4.99, 5.11, 5.23,
    5.36, 5.49, 5.62, 5.76, 5.90, 6.04, 6.19, 6.34, 6.49, 6.65,
    6.81, 6.98, 7.15, 7.32, 7.50, 7.68, 7.87, 8.06, 8.25, 8.45,
    8.66, 8.87, 9.09, 9.31, 9.53, 9.76
]

def calculate_voltage(r1, r2):
    return 1.25 * (1 + (r2 / r1))

def find_best_combinations(desired_volt, resistor_series):
    results = []
    seen_ratios = set()  # To track ratios we've already considered

    # Expanding the E96 series by considering 100x multipliers
    # because the LM317 can only handle 1.5A of current
    # R1 may be any value between 100 Ohm and 10k Ohm
    # R2 may be any value between 100 Ohm and 10k Ohm
    expanded_resistor_set = [val * multiplier for multiplier in [100] for val in resistor_series]
    
    for r1 in expanded_resistor_set:
        for r2 in expanded_resistor_set:
            if r1 != r2:  # to prevent divide by zero and identical combinations
                ratio = round(r1 / r2, 6)  # 6 decimal places should be sufficient for precision
                
                if ratio not in seen_ratios:
                    seen_ratios.add(ratio)
                    volt = calculate_voltage(r1, r2)
                    error = abs(volt - desired_volt)
                    diff = volt - desired_volt
                    results.append((r1, r2, volt, error, diff))
                    
    results.sort(key=lambda x: x[3])  # Sort by error
    return results[:20]

def main():
    desired_volt = float(input("Enter desired voltage: "))
    combinations = find_best_combinations(desired_volt, E24)

    print("Top 10 unique resistor combinations from expanded E24 series:")
    for r1, r2, volt, error, diff in combinations:
        print(f"R1: {r1:.2f} Ohm, R2: {r2:.2f} Ohm, Voltage: {volt:.4f} V, Diff: {diff:.4f} V")

    combinations = find_best_combinations(desired_volt, E96)
    print("")
    print("Top 10 unique resistor combinations from expanded E96 series:")
    for r1, r2, volt, error, diff in combinations:
        print(f"R1: {r1:.2f} Ohm, R2: {r2:.2f} Ohm, Voltage: {volt:.4f} V, Diff: {diff:.4f} V")

if __name__ == "__main__":
    main()
