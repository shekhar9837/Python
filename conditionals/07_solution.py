

coffeeSize = input("Please provide size of coffee, Small Medium, Large : ")

print("want with Extra shot?")
option = input("Please provide Extra shot")

if coffeeSize == "Small":
    print("Cost: $3")
    if option == "Extra shot":
        print("Extra shot costs an additional $1")
        print("Total cost: $4")
elif coffeeSize == "Medium":
    print("Cost: $4")
    if option == "Extra shot":
        print("Extra shot costs an additional $1")
        print("Total cost: $5")
elif coffeeSize == "Large":
    print("Cost: $5")
    if option == "Extra shot":
        print("Extra shot costs an additional $1")
        print("Total cost: $6")
else:
    print("Invalid option")