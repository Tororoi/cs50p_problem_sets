def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # Reformat the string to remove the dollar sign and convert to float
    return float(d.lstrip('$'))


def percent_to_float(p):
    # Reformat the string to remove the percentage sign and convert to float
    return float(p.rstrip('%')) / 100


main()
