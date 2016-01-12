from scraper import getStats

a = input("What yahoo finance url would you like to use?: ")
print("\n")
valuation = getStats(a)
for row in valuation:
    for column in row:
        print(column, end=" ")
    print("\n")
print("Thank you")