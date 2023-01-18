def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(
        input("What percentage would you like to tip? "))
    tip = (dollars * percent) / int(100)

    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    d = d.replace("$", "")
    d = int(float(d))
    return d


def percent_to_float(p):
    p = p.replace("%", "")
    p = int(float(p))
    return p


main()
