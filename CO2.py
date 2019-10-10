import statistics

def air_quality():
    level = int(input("Please input air quality value: "))
    if level > 399 and level < 698:
        print("Excelent")
    elif level > 699 and level < 898:
        print("Good")
    elif level > 899 and level < 1098:
        print("Fair")
    elif level > 1099 and level < 1598:
        print("Mediocre, contaminated indoor air")
    elif level > 1599 and level < 2101:
        print("Bad, heavily contaminated indoor air")

air_quality()
