

distance  = input("enter a distance")

distance = int(distance)

if distance < 3:
    print("Walk")
elif distance < 15:
    print("Bike")
elif distance > 15:
    print("Car")
else:
    print("Invalid")