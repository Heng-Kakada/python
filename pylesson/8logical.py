# logical operator (and,or) used to check if two or more conditional statements is true

temp = int(input("what is the temperature outside? :"))

# bigger 0 and less 30 good


if temp >= 0 and temp <= 30:
    print("today temperature is good")
elif temp < 0 or temp > 30:
    print("today temperature is bad")
