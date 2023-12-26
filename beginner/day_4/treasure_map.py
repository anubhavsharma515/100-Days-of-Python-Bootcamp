import random

line1 = ["⬜️", "⬜️", "⬜️"]
line2 = ["⬜️", "⬜️", "⬜️"]
line3 = ["⬜️", "⬜️", "⬜️"]

treasure_map = [line1,line2,line3]

print("Where's your treasure? X marks the spot")
treasure_coordinates = input()

treasure_x_coordinate = treasure_coordinates[0]
treasure_y_coordinate = int(treasure_coordinates[1])

if treasure_x_coordinate == 'A':
  treasure_map[treasure_y_coordinate-1][0] = 'X'
elif treasure_x_coordinate == 'B':
  treasure_map[treasure_y_coordinate-1][1] = 'X'
elif treasure_x_coordinate == 'C':
  treasure_map[treasure_y_coordinate-1][2] = 'X'

print(treasure_map[0])
print(treasure_map[1])
print(treasure_map[2])
