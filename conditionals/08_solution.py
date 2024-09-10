

password = "4536"


if len(password) < 6:
    strength = "weak"
elif len(password) <= 10:
    strength  =  "moderate"
else:
    strength ="strong"

print("strength " + strength)