print("Welcome to the Band Name Generator")


city = input("What's name of the city you grew up in?\n")
band = input("What's your pets name?\n")

# Print Options
#print(f"Your band name is {city} {band}")
#print("Your band name is %s %s" % (city.capitalize(), band.capitalize()))
print("Your band name is {} {}".format(city.capitalize(), band.capitalize()))

