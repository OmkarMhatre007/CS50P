def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage of discount is applied ? "))
    final_price = dollars - ((percent/100) * dollars)
    print(f"Pay ${final_price:.2f}")


def dollars_to_float(d):
    # TODO
    return float(d.replace("$", ""))

def percent_to_float(p):
    # TODO
    return float(p.replace("%", ""))

main()

# 100
# 20
# 20/100 *100